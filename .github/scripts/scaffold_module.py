#!/usr/bin/env python3
"""Scaffold a new GeLS AppModule from the template/ folder.

Driven by the "New Module" GitHub Action. Given the development branch name
(e.g. ``development/PM_02_47_MOTOR_DRIVER_BTM9011EP``) this derives the module
names (index name, number, snake, PascalCase, etc.) and copies ``template/``
-> ``development/AppModules/<PascalName>/`` with the files renamed and the
placeholders substituted.

This module also holds the shared name-derivation and AppModules.h/.c editing
logic (register_header/register_source) used by register_module.py, which
registers the module directly on main -- see that script for why registration
is handled separately from this one.

File scaffolding is idempotent: it is skipped if the destination folder
already exists, so re-running this (or a second push) is a no-op.

Usage:
    python scaffold_module.py <branch-name>
"""

import os
import re
import shutil
import sys
from datetime import datetime

# ---------------------------------------------------------------------------
# Repository layout (relative to repo root, which is the working directory).
# ---------------------------------------------------------------------------
TEMPLATE_DIR = "template"
DEV_MODULES_DIR = os.path.join("development", "AppModules")
APP_MODULES_H = os.path.join("exempt", "AppModules", "AppModules", "AppModules.h")
APP_MODULES_C = os.path.join("exempt", "AppModules", "AppModules", "AppModules.c")

DEV_BRANCH_PREFIX = "development/"
# AM_01_02 / PM_02_47 / PM_02_15a ...
NUMBER_PREFIX_RE = re.compile(r"^([AP]M_\d+_\d+[a-z]?)_(.+)$")


def fail(message):
    print(f"::error::{message}")
    sys.exit(1)


def set_output(**kwargs):
    """Expose values to later workflow steps via $GITHUB_OUTPUT."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


# ---------------------------------------------------------------------------
# Name derivation
# ---------------------------------------------------------------------------
def derive_pascal(snake):
    """Convert SCREAMING_SNAKE_CASE to the PascalCase module name.

    Keeps a trailing hardware-model token (one containing a digit) UPPERCASE,
    separated by an underscore. E.g. MOTOR_DRIVER_BTM9011EP -> MotorDriver_BTM9011EP.
    """
    tokens = [t for t in snake.split("_") if t]
    if not tokens:
        fail(f"Could not derive a module name from '{snake}'.")

    model = None
    lead = tokens
    if any(ch.isdigit() for ch in tokens[-1]):
        model = tokens[-1]
        lead = tokens[:-1]

    core = "".join(t[:1].upper() + t[1:].lower() for t in lead)
    if model:
        return f"{core}_{model}" if core else model
    return core


def derive_names(branch):
    if not branch.startswith(DEV_BRANCH_PREFIX):
        fail(
            f"Branch '{branch}' is not a new-module branch "
            f"(expected '{DEV_BRANCH_PREFIX}<INDEX_NAME>')."
        )

    index_name = branch[len(DEV_BRANCH_PREFIX):].strip().strip("/")
    match = NUMBER_PREFIX_RE.match(index_name)
    if not match:
        fail(
            f"Branch '{branch}' does not match the naming convention "
            f"'{DEV_BRANCH_PREFIX}<AM|PM>_<group>_<num>_<NAME>', "
            f"e.g. '{DEV_BRANCH_PREFIX}PM_02_47_MOTOR_DRIVER_BTM9011EP'."
        )

    number = match.group(1)
    snake = match.group(2)
    pascal = derive_pascal(snake)
    camel = pascal[:1].lower() + pascal[1:]
    group = f"{number}_{pascal}"

    now = datetime.now()
    return {
        "__MODULE_INDEX_NAME__": index_name,
        "__MODULE_NUMBER__": number,
        "__MODULE_SNAKE__": snake,
        "__MODULE_PASCAL__": pascal,
        "__MODULE_CAMEL__": camel,
        "__MODULE_GROUP__": group,
        "__YEAR__": now.strftime("%Y"),
        "__DATE__": now.strftime("%d-%b-%Y"),
    }


def substitute(text, names):
    for placeholder, value in names.items():
        text = text.replace(placeholder, value)
    return text


# ---------------------------------------------------------------------------
# File scaffolding
# ---------------------------------------------------------------------------
def scaffold_files(names):
    pascal = names["__MODULE_PASCAL__"]
    dest_root = os.path.join(DEV_MODULES_DIR, pascal)

    if os.path.isdir(dest_root):
        print(f"Module folder already exists: {dest_root} (skipping file scaffold).")
        return False

    if not os.path.isdir(TEMPLATE_DIR):
        fail(f"Template folder not found: {TEMPLATE_DIR}")

    for current_dir, _dirs, files in os.walk(TEMPLATE_DIR):
        rel_dir = os.path.relpath(current_dir, TEMPLATE_DIR)
        rel_dir = "" if rel_dir == "." else substitute(rel_dir, names)
        target_dir = os.path.join(dest_root, rel_dir)
        os.makedirs(target_dir, exist_ok=True)

        for file_name in files:
            # README.md documents the template itself; do not copy it out.
            if rel_dir == "" and file_name == "README.md":
                continue

            src_path = os.path.join(current_dir, file_name)
            target_name = substitute(file_name, names)
            target_path = os.path.join(target_dir, target_name)

            if is_binary(src_path):
                shutil.copy2(src_path, target_path)
            else:
                with open(src_path, "r", encoding="utf-8") as handle:
                    content = handle.read()
                with open(target_path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(substitute(content, names))

    print(f"Scaffolded module files into {dest_root}")
    return True


def is_binary(path):
    with open(path, "rb") as handle:
        return b"\x00" in handle.read(4096)


# ---------------------------------------------------------------------------
# AppModules.h / AppModules.c registration
# ---------------------------------------------------------------------------
def _format_define(name, value, value_col):
    line = f"#define {name}"
    if len(line) < value_col:
        line += " " * (value_col - len(line))
    else:
        line += " "
    return f"{line}{value}U"


def register_header(names):
    macro = f"APP_MODULES__{names['__MODULE_INDEX_NAME__']}_INDEX"

    with open(APP_MODULES_H, "r", encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    if any(macro in line for line in lines):
        print(f"{macro} already present in AppModules.h (skipping header edit).")
        return False, None

    count_re = re.compile(r"^#define\s+APP_MODULES__NUMBER_OF_MODULES\s+(\d+)U\s*$")
    for idx, line in enumerate(lines):
        m = count_re.match(line)
        if m:
            new_index = int(m.group(1))
            new_count = new_index + 1
            value_col = line.rstrip().rfind(f"{new_index}U")
            if value_col < 0:
                value_col = 67
            define_line = _format_define(macro, new_index, value_col)
            count_line = _format_define(
                "APP_MODULES__NUMBER_OF_MODULES", new_count, value_col
            )
            lines[idx : idx + 1] = [define_line, count_line]
            with open(APP_MODULES_H, "w", encoding="utf-8", newline="\n") as handle:
                handle.write("\n".join(lines))
            print(f"Registered {macro} = {new_index}U in AppModules.h")
            return True, new_index

    fail("Could not find APP_MODULES__NUMBER_OF_MODULES in AppModules.h")


def register_source(names, new_index):
    index_name = names["__MODULE_INDEX_NAME__"]
    entry_string = f'"{index_name}"'

    with open(APP_MODULES_C, "r", encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    if any(entry_string in line for line in lines):
        print(f"{entry_string} already present in AppModules.c (skipping source edit).")
        return False

    # Locate the COMPILE_MODULE_NAMES #if / #else / #endif fences.
    idx_if = _find(lines, lambda s: s.strip().startswith("#if")
                   and "COMPILE_MODULE_NAMES" in s, 0)
    idx_else = _find(lines, lambda s: s.strip() == "#else", idx_if + 1)
    idx_endif = _find(lines, lambda s: s.strip().startswith("#endif")
                      and "COMPILE_MODULE_NAMES" in s, idx_else + 1)
    if -1 in (idx_if, idx_else, idx_endif):
        fail("Could not locate the COMPILE_MODULE_NAMES block in AppModules.c")

    # --- Named-string entry (inserted before #else) -----------------------
    name_entry_re = re.compile(r'^(\s*)"[^"]*",\s*//\s*\d+\s*$')
    comment_col = None
    indent = "   "
    for line in lines[idx_if + 1 : idx_else]:
        m = name_entry_re.match(line)
        if m:
            indent = m.group(1)
            comment_col = line.find("//")
    name_line = f'{indent}{entry_string},'
    if comment_col is not None:
        if len(name_line) < comment_col:
            name_line += " " * (comment_col - len(name_line))
        else:
            name_line += " "
        name_line += f"// {new_index}"

    # --- Numeric-string entry (inserted before #endif) --------------------
    num_entry_re = re.compile(r'^(\s*)"\d+",\s*$')
    num_indent = "   "
    last_num_idx = None
    for j in range(idx_else + 1, idx_endif):
        m = num_entry_re.match(lines[j])
        if m:
            num_indent = m.group(1)
            last_num_idx = j
    num_line = f'{num_indent}"{new_index}",'

    # Insert numeric entry first (it is below #else, so idx_else is unchanged).
    if last_num_idx is not None:
        lines.insert(last_num_idx + 1, num_line)
    else:
        lines.insert(idx_endif, num_line)
    lines.insert(idx_else, name_line)

    with open(APP_MODULES_C, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    print(f"Registered string entries for index {new_index} in AppModules.c")
    return True


def _find(lines, predicate, start):
    for i in range(start, len(lines)):
        if predicate(lines[i]):
            return i
    return -1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        fail("Usage: scaffold_module.py <branch-name>")

    branch = sys.argv[1].strip()
    names = derive_names(branch)

    print(f"Index name : {names['__MODULE_INDEX_NAME__']}")
    print(f"Number     : {names['__MODULE_NUMBER__']}")
    print(f"Snake      : {names['__MODULE_SNAKE__']}")
    print(f"Pascal     : {names['__MODULE_PASCAL__']}")
    print(f"Doxy group : {names['__MODULE_GROUP__']}")

    changed = scaffold_files(names)
    set_output(
        changed=str(changed).lower(),
        module=names["__MODULE_PASCAL__"],
        index_name=names["__MODULE_INDEX_NAME__"],
    )
    print(f"Done. changed={changed}")


def _existing_index(names):
    macro = f"APP_MODULES__{names['__MODULE_INDEX_NAME__']}_INDEX"
    pattern = re.compile(re.escape(macro) + r"\s+(\d+)U")
    with open(APP_MODULES_H, "r", encoding="utf-8") as handle:
        m = pattern.search(handle.read())
    return int(m.group(1)) if m else None


if __name__ == "__main__":
    main()

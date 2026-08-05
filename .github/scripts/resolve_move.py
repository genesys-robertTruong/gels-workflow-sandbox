#!/usr/bin/env python3
"""Resolve whether a merged PR should promote a module folder, and to where.

Used by the "Module Folder Promotion" workflow. On a merged new-module PR the
module lives in development/AppModules/<Module>; once accepted it is moved to
certified/AppModules/<Module> (label "iec62304") or functional/AppModules/<Module>
(label "functional"). Maintenance labels keep the module in place, so they
resolve to "no move".

Usage:
    python resolve_move.py "<head-branch>" '<labels-json-array>'

Outputs (via $GITHUB_OUTPUT): move, module, src, dest, dest_root
"""

import json
import os
import re
import sys

# Reuse the exact naming logic the scaffolder uses.
from scaffold_module import derive_pascal, NUMBER_PREFIX_RE

# A promotable module lives in development/ on a development/<INDEX_NAME>
# branch -- whether it was newly scaffolded, resumed from deferred, or
# re-graded up from functional/ (all three share the development/ prefix; see
# new-module.yml).
DEV_PREFIXES = ("development/",)

# Review label -> destination top-level folder.
LABEL_DEST = {
    "iec62304": "certified",
    "functional": "functional",
}
DEV_ROOT = "development/AppModules"


def set_output(**kwargs):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


def find_source(pascal, snake):
    """Locate the module folder in development/, tolerating manual renames.

    Mirrors the CMake "fuzzy match" (compare names with separators stripped),
    so e.g. an ICM_20648-style folder is still found.
    """
    direct = f"{DEV_ROOT}/{pascal}"
    if os.path.isdir(direct):
        return direct

    if os.path.isdir(DEV_ROOT):
        target = re.sub(r"[^A-Z0-9]", "", snake.upper())
        for name in sorted(os.listdir(DEV_ROOT)):
            full = f"{DEV_ROOT}/{name}"
            if os.path.isdir(full) and re.sub(r"[^A-Z0-9]", "", name.upper()) == target:
                return full
    return None


def main():
    if len(sys.argv) != 3:
        print("::error::Usage: resolve_move.py <head-branch> <labels-json>")
        sys.exit(1)

    branch = sys.argv[1].strip()
    try:
        labels = json.loads(sys.argv[2] or "[]")
    except json.JSONDecodeError:
        labels = []

    dest_root = next((LABEL_DEST[name] for name in labels if name in LABEL_DEST), None)
    if not dest_root:
        print("No promotion label (iec62304/functional) on PR; nothing to move.")
        set_output(move="false")
        return

    prefix = next((p for p in DEV_PREFIXES if branch.startswith(p)), None)
    if not prefix:
        print(f"::warning::'{dest_root}' promotion label present but head branch "
              f"'{branch}' is not a {' / '.join(DEV_PREFIXES)} branch; skipping move.")
        set_output(move="false")
        return

    index_name = branch[len(prefix):].strip().strip("/")
    match = NUMBER_PREFIX_RE.match(index_name)
    if not match:
        print(f"::warning::Could not parse a module name from '{branch}'; skipping move.")
        set_output(move="false")
        return

    snake = match.group(2)
    pascal = derive_pascal(snake)
    src = find_source(pascal, snake)
    if not src:
        print(f"::warning::No module folder for '{pascal}' under {DEV_ROOT}; "
              f"nothing to move (already promoted?).")
        set_output(move="false")
        return

    module = os.path.basename(src)
    dest = f"{dest_root}/AppModules/{module}"
    print(f"Will move {src} -> {dest}")
    set_output(move="true", module=module, src=src, dest=dest, dest_root=dest_root)


if __name__ == "__main__":
    main()

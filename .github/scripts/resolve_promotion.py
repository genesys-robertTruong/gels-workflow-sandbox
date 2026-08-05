#!/usr/bin/env python3
"""Resolve a functional -> development promotion move.

Used by the "Module Promotion" workflow. Pushing a branch named
``promotion/<INDEX_NAME>`` (e.g. ``promotion/PM_02_47_MOTOR_DRIVER_BTM9011EP``)
moves the module from ``functional/AppModules/<Module>`` back into
``development/AppModules/<Module>`` so it can go through the full IEC 62304
development process. History is preserved by the workflow's ``git mv``.

Usage:
    python resolve_promotion.py "<branch>"

Outputs (via $GITHUB_OUTPUT): move, module, src, dest
"""

import os
import re
import sys

from scaffold_module import derive_pascal, NUMBER_PREFIX_RE

PROMOTION_PREFIX = "promotion/"
SRC_ROOT = "functional/AppModules"
DEST_ROOT = "development/AppModules"


def set_output(**kwargs):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


def fuzzy_find(root, pascal, snake):
    """Find a module folder under root, tolerating manual renames (matches the
    CMake scan: compare names with separators stripped)."""
    direct = f"{root}/{pascal}"
    if os.path.isdir(direct):
        return direct
    if os.path.isdir(root):
        target = re.sub(r"[^A-Z0-9]", "", snake.upper())
        for name in sorted(os.listdir(root)):
            full = f"{root}/{name}"
            if os.path.isdir(full) and re.sub(r"[^A-Z0-9]", "", name.upper()) == target:
                return full
    return None


def main():
    if len(sys.argv) != 2:
        print("::error::Usage: resolve_promotion.py <branch>")
        sys.exit(1)

    branch = sys.argv[1].strip()
    if not branch.startswith(PROMOTION_PREFIX):
        print(f"::warning::Branch '{branch}' is not a {PROMOTION_PREFIX} branch; nothing to do.")
        set_output(move="false")
        return

    index_name = branch[len(PROMOTION_PREFIX):].strip().strip("/")
    match = NUMBER_PREFIX_RE.match(index_name)
    if not match:
        print(f"::warning::Could not parse a module name from '{branch}'; nothing to do.")
        set_output(move="false")
        return

    snake = match.group(2)
    pascal = derive_pascal(snake)

    src = fuzzy_find(SRC_ROOT, pascal, snake)
    if not src:
        # Already moved into development (e.g. a re-push)?
        if fuzzy_find(DEST_ROOT, pascal, snake):
            print(f"'{pascal}' is already in {DEST_ROOT} (skipping).")
        else:
            print(f"::warning::No module folder for '{pascal}' under {SRC_ROOT}; "
                  f"nothing to promote.")
        set_output(move="false")
        return

    module = os.path.basename(src)
    dest = f"{DEST_ROOT}/{module}"
    if os.path.exists(dest):
        print(f"::warning::Destination {dest} already exists; skipping move.")
        set_output(move="false")
        return

    print(f"Will move {src} -> {dest}")
    set_output(move="true", module=module, src=src, dest=dest)


if __name__ == "__main__":
    main()

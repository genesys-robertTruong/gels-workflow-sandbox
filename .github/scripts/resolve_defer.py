#!/usr/bin/env python3
"""Resolve which module a defer PR's head branch identifies.

Used by the Defer Module Cleanup workflow. To defer a module you open a PR
directly from its existing development/<INDEX_NAME> branch, base
deferred/snapshot -- no manual git mv needed. The module being deferred is
identified from that head branch name, the same way every other GeLS
automation derives module identity from a branch (see scaffold_module.py,
resolve_move.py).

Usage:
    python resolve_defer.py <head-branch>

Outputs (via $GITHUB_OUTPUT): module
"""

import os
import sys

from scaffold_module import derive_names


def set_output(**kwargs):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


def main():
    if len(sys.argv) != 2:
        print("::error::Usage: resolve_defer.py <head-branch>")
        sys.exit(1)

    names = derive_names(sys.argv[1].strip())
    module = names["__MODULE_PASCAL__"]
    print(f"Resolved deferred module: {module}")
    set_output(module=module)


if __name__ == "__main__":
    main()

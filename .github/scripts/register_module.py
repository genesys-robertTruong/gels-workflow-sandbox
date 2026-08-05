#!/usr/bin/env python3
"""Register a module's index in AppModules.h/.c -- directly on main.

Run by the New Module workflow immediately when a module is scaffolded,
against a checkout of main rather than the development/<INDEX_NAME> branch.
AppModules.h and AppModules.c live under exempt/, outside the normal
per-module review process, so their index reservation is intentionally
global and immediate: main always knows about every module that has ever
been scaffolded, whether it is still in development, has been promoted, or
has been deferred.

This is what keeps two modules scaffolded around the same time -- or a
deferred module and a later one -- from ever claiming the same index. A
deferred module's registration is never removed (see defer-module-cleanup.yml,
which only removes the *folder* from development/ on main), so main's next
scaffold always sees it and picks the next index correctly.

Idempotent: a module already registered is left untouched, so re-running
this for an existing module (e.g. on resume, where registration already
happened at the original scaffold) is always a safe no-op.

Usage:
    python register_module.py <branch-name>

Outputs (via $GITHUB_OUTPUT): changed, module, index_name
"""

import sys

from scaffold_module import (
    derive_names,
    register_header,
    register_source,
    set_output,
    _existing_index,
)


def main():
    if len(sys.argv) != 2:
        print("::error::Usage: register_module.py <branch-name>")
        sys.exit(1)

    names = derive_names(sys.argv[1].strip())

    header_changed, new_index = register_header(names)
    if new_index is None:
        # Header already had the macro; recover its index for the .c registration.
        new_index = _existing_index(names)
    source_changed = register_source(names, new_index) if new_index is not None else False

    changed = header_changed or source_changed
    set_output(
        changed=str(changed).lower(),
        module=names["__MODULE_PASCAL__"],
        index_name=names["__MODULE_INDEX_NAME__"],
    )
    print(f"Done. changed={changed}")


if __name__ == "__main__":
    main()

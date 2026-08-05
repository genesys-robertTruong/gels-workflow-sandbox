#!/usr/bin/env python3
"""Re-grade a functional module back into development for IEC 62304.

Run by the New Module workflow BEFORE scaffold_module.py, on every push to a
development/<INDEX_NAME> branch. If the module currently lives in
functional/AppModules/<Module> on this branch (which mirrors main) and is not
already in development/AppModules/, it is git-moved into development/ so it can
go through the full IEC 62304 development process. The move lands on main when
the eventual iec62304 review PR is merged (module-folder-move then promotes it
on to certified/).

This unifies the "re-grade functional -> development" flow with the "new
module" and "resume from deferred" flows: all three are just a push to
development/<INDEX_NAME>, and the source is inferred from where the module
currently lives (deferred/ -> functional/ -> brand new). A module is only ever
in one of those states, so the inference is unambiguous. This replaces the old
promotion/<INDEX_NAME> branch and module-promotion.yml.

If the module is not in functional/, this is a no-op; restore_from_deferred.py
and scaffold_module.py handle the resume and new-module cases.

Usage:
    python regrade_from_functional.py <branch-name>

Outputs (via $GITHUB_OUTPUT): regraded, module, index_name
"""

import os
import subprocess
import sys

from scaffold_module import derive_names, DEV_MODULES_DIR

FUNCTIONAL_MODULES_DIR = os.path.join("functional", "AppModules")


def set_output(**kwargs):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


def main():
    if len(sys.argv) != 2:
        print("::error::Usage: regrade_from_functional.py <branch-name>")
        sys.exit(1)

    names = derive_names(sys.argv[1].strip())
    pascal = names["__MODULE_PASCAL__"]

    dev_dest = os.path.join(DEV_MODULES_DIR, pascal)
    if os.path.isdir(dev_dest):
        # Already in development (a resume/re-grade already ran, or a re-push).
        print(f"{dev_dest} already exists; nothing to re-grade.")
        set_output(regraded="false")
        return

    src = os.path.join(FUNCTIONAL_MODULES_DIR, pascal)
    if not os.path.isdir(src):
        print(f"{pascal} not found under {FUNCTIONAL_MODULES_DIR}; not a re-grade.")
        set_output(regraded="false")
        return

    print(f"Re-grading {src} -> {dev_dest} (functional -> development for IEC 62304).")
    os.makedirs(DEV_MODULES_DIR, exist_ok=True)
    subprocess.run(["git", "mv", src, dev_dest], check=True)

    set_output(regraded="true", module=pascal, index_name=names["__MODULE_INDEX_NAME__"])


if __name__ == "__main__":
    main()

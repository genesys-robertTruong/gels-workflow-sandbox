#!/usr/bin/env python3
"""Restore a module from deferred/AppModules/ if it was previously deferred.

Run by the New Module workflow BEFORE scaffold_module.py, on every push to a
development/<INDEX_NAME> branch. If the module already exists under
deferred/AppModules/ on the deferred/snapshot branch, this moves it back into
development/AppModules/ on the current branch (a git mv from a checkout of
just that path) so development can resume. scaffold_module.py then sees the
destination folder already exists and skips re-scaffolding from template/,
but still runs its (idempotent) AppModules.h/.c registration step -- which is
a no-op here since deferring never removes that registration.

If no deferred copy exists, this is a plain no-op and scaffold_module.py
proceeds with a normal brand-new scaffold, exactly as before this script
existed.

Usage:
    python restore_from_deferred.py <branch-name>

Outputs (via $GITHUB_OUTPUT): restored, module, index_name
"""

import os
import subprocess
import sys

from scaffold_module import derive_names, DEV_MODULES_DIR

DEFERRED_REF = "origin/deferred/snapshot"
DEFERRED_MODULES_DIR = "deferred/AppModules"


def set_output(**kwargs):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in kwargs.items():
            handle.write(f"{key}={value}\n")


def exists_on_deferred(pascal):
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{DEFERRED_REF}:{DEFERRED_MODULES_DIR}/{pascal}"],
        capture_output=True,
    )
    return result.returncode == 0


def main():
    if len(sys.argv) != 2:
        print("::error::Usage: restore_from_deferred.py <branch-name>")
        sys.exit(1)

    branch = sys.argv[1].strip()
    names = derive_names(branch)
    pascal = names["__MODULE_PASCAL__"]

    subprocess.run(["git", "fetch", "origin", "deferred/snapshot"], check=True)

    if not exists_on_deferred(pascal):
        print(f"{pascal} not found under {DEFERRED_MODULES_DIR}/ on deferred/snapshot; not a resume.")
        set_output(restored="false")
        return

    dest = os.path.join(DEV_MODULES_DIR, pascal)
    if os.path.isdir(dest):
        print(f"{dest} already exists on this branch; leaving it as-is (not overwriting from deferred/).")
        set_output(restored="false")
        return

    print(f"Found {pascal} under deferred/AppModules/ on deferred/snapshot; restoring to {dest}.")
    src = f"{DEFERRED_MODULES_DIR}/{pascal}"
    subprocess.run(["git", "checkout", DEFERRED_REF, "--", src], check=True)
    os.makedirs(DEV_MODULES_DIR, exist_ok=True)
    subprocess.run(["git", "mv", src, dest], check=True)

    set_output(restored="true", module=pascal, index_name=names["__MODULE_INDEX_NAME__"])


if __name__ == "__main__":
    main()

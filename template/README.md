# Module Template

This folder is the source template used by the **New Module** GitHub Action
(`.github/workflows/new-module.yml` + `.github/scripts/scaffold_module.py`).

When a branch named `development/<INDEX_NAME>` is pushed (e.g.
`development/PM_02_47_MOTOR_DRIVER_BTM9011EP`), the action copies this folder
into `development/AppModules/<ModuleName>/` **on that branch**, renames the
files, and substitutes the placeholders below.

The module is developed on the `development/*` branch and stays in the
`development/AppModules/` folder for the whole development process. It only
reaches the default branch when the review PR is merged at the end, at which
point automation moves it to `certified/` or `functional/`.

## Placeholders

| Placeholder              | Example                                | Meaning                                                              |
| ------------------------ | -------------------------------------- | ------------------------------------------------------------------- |
| `__MODULE_INDEX_NAME__`  | `PM_02_47_MOTOR_DRIVER_BTM9011EP`      | Full index name (the branch name minus the `development/` prefix).   |
| `__MODULE_NUMBER__`      | `PM_02_47`                             | The `AM_xx_xx` / `PM_xx_xx[a]` number prefix.                       |
| `__MODULE_SNAKE__`       | `MOTOR_DRIVER_BTM9011EP`               | SCREAMING_SNAKE name (index name without the number prefix).        |
| `__MODULE_PASCAL__`      | `MotorDriver_BTM9011EP`                | PascalCase folder / file / C-identifier base.                       |
| `__MODULE_CAMEL__`       | `motorDriver_BTM9011EP`                | camelCase variant (PascalCase with a lower-case first letter).      |
| `__MODULE_GROUP__`       | `PM_02_47_MotorDriver_BTM9011EP`       | Doxygen group: number prefix + PascalCase.                          |
| `__YEAR__`               | `2026`                                 | Year the module was scaffolded.                                     |
| `__DATE__`               | `29-May-2026`                          | Date the module was scaffolded.                                     |

## PascalCase derivation rule

`__MODULE_SNAKE__` is converted to `__MODULE_PASCAL__` using a "digit-suffix"
heuristic that matches the existing modules:

1. Split the snake name on `_`.
2. If the **last** token contains a digit it is treated as the hardware model
   (e.g. `BTM9011EP`, `LIS2DH`, `BQ25890H`) and is kept UPPERCASE, preceded by
   an underscore.
3. Every remaining leading token is capitalised and concatenated (no
   underscores): `MOTOR`, `DRIVER` -> `MotorDriver`.

Result: `MOTOR_DRIVER_BTM9011EP` -> `MotorDriver_BTM9011EP`.

> **Edge case:** models whose code is split across two tokens (e.g.
> `..._ICM_20648`) only keep the final digit token as the model
> (`...Icm_20648`). Rename the generated folder/files by hand in those rare
> cases.

## What the action also does

* Creates the module under `development/AppModules/<ModuleName>/` (the basic
  `.c/.h`, test files, `CMakeLists.txt` and the `Design/` folder).
* Auto-registers the module in `exempt/AppModules/AppModules/AppModules.h` and
  `AppModules.c` (index `#define`, `NUMBER_OF_MODULES` bump and string-lookup
  entries).
* Commits and pushes the result back onto the same `development/*` branch.

The action is idempotent: if the module folder and registry entry already exist
it does nothing.

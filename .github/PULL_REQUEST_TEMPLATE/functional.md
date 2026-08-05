<!-- gels-review-type: functional -->
<!-- Do not delete the line above: it tells the merge gate which checklist applies and sets the `functional` label. -->

# Functional Review

Sanity-check review for a **new module** destined for `functional/` (not full
IEC 62304). Covers the Development checklist up to step 6 plus basic testing.

**Module (index name):**
**Jira ticket (GDRP):**

> The merge gate blocks this PR until every checkbox below is ticked. For items
> that genuinely do not apply, tick the box and write `N/A — <reason>` next to it.

## Setup
- [ ] Module scaffolded on a `development/<INDEX_NAME>` branch — the New Module action created the files and registered the module in `AppModules.c/.h`.
- [ ] `APP_MODULES_CONFIG__ENABLE_<INDEX_NAME>` `#define` added in the app-side `Config.h`.
- [ ] `UnitTestManager.c/.h` updated: `#define` in `.h`, gated `#include` in `.c`, element added to `TestModulesArray_gro`.
- [ ] (PIOS only) New driver/port files added and `PIOS.h` updated — or `N/A` (not a PIOS driver).

## Documentation & requirements
- [ ] `.dox` header fields filled: file / author / version / date / brief.
- [ ] "Module Requirements and Tests" tab filled out.
- [ ] Function APIs defined in `module.h`, each with a Doxygen `@brief` / `@param` / `@return`.
- [ ] Jira ticket created on the [GDRP board](https://genesysdesign.atlassian.net/jira/software/c/projects/GDRP/boards/16) and linked above.

## Implementation & basic test
- [ ] Functionality implemented in `module.c/.h` (step 6).
- [ ] Basic testing performed (functional sanity check) with evidence in `Design/TestOutput/`.

---
### On merge (reviewer / automation — not gated)
- With the `functional` label, automation moves the module from `development/` to `functional/`.
- Reviewer completes a sanity-check review and deletes the `development/*` branch.
- **Reviewer sets the Jira ticket to the correct state** once the merge is complete.

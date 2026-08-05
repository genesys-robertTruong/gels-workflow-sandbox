<!-- gels-review-type: iec62304-maintenance -->
<!-- Do not delete the line above: it tells the merge gate which checklist applies and sets the `iec62304-maintenance` label. -->

# IEC 62304 Maintenance Review

Full GeLS maintenance review for a change to a **released module in `certified/`**.
Source of truth: *Software Development and Review Checklist* (Maintenance tab).

**Module (index name):**
**Jira ticket(s) (GDRP):**
**Maintenance type:** <!-- Subminor / Minor / Major — per GD-0008-MAN1 §6.1.2 -->

> The merge gate blocks this PR until every checkbox below is ticked. For items
> that genuinely do not apply, tick the box and write `N/A — <reason>` next to it.

## Pre-maintenance
- [ ] Maintenance branch created as `maintenance/<INDEX_NAME>+<JIRA_ID>` from the latest `certified/` version.
- [ ] Maintenance type recorded above (Subminor / Minor / Major) per GD-0008-MAN1 §6.1.2.
- [ ] Jira ticket(s) advanced to **IN PROGRESS**.

## Maintenance actions
- [ ] Required functional change implemented in the module.
- [ ] Version number and date updated in `module.dox` **and** the checklist cover sheet.
- [ ] Config files updated in the corresponding AppModuleConfig branch — or `N/A`.
- [ ] Confirmed `certified/` has not changed since branching; if it had, the maintenance branch was **rebased** onto the latest `certified/` (rebase — not a merge commit) and version numbers are still accurate.
- [ ] Test results and MISRA results updated in the relevant `Design/` folders.
- [ ] (Subminor / Minor) Backwards-compatibility considerations taken into account.
- [ ] (Minor / Major) Module requirements updated in "Module Requirements and Tests" tab — or `N/A`.
- [ ] (Minor / Major) Test details updated in "Module Requirements and Tests" tab — or `N/A`.
- [ ] (Minor / Major) Requirements / tests / test-code signoff cleared and re-signed — or `N/A`.
- [ ] (Minor / Major) `module.h` and `module.dox` documentation updated — or `N/A`.
- [ ] (Minor / Major) Review checklist cleared and repopulated — or `N/A`.
- [ ] Jira ticket(s) advanced to **READY FOR REVIEW**.

## Integration
- [ ] Integrated and tested in a template project (list in comments) — or `N/A`.

---
### On merge (reviewer / automation — not gated)
- Merge to `certified/` (commit must contain the version number); delete the maintenance branch.
- Alert template-project owner(s); move the relevant Jira tickets from RESOLVED.
- (Major change) Inform relevant teams of the non-backwards-compatible change (e.g. all-staff email).

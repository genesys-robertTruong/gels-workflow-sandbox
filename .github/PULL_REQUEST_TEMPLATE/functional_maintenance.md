<!-- gels-review-type: functional-maintenance -->
<!-- Do not delete the line above: it tells the merge gate which checklist applies and sets the `functional-maintenance` label. -->

# Functional Maintenance Review

Sanity-check maintenance review for a change to a module in `functional/` (not
full IEC 62304). Light subset of the Maintenance checklist.

**Module (index name):**
**Jira ticket(s) (GDRP):**

> The merge gate blocks this PR until every checkbox below is ticked. For items
> that genuinely do not apply, tick the box and write `N/A — <reason>` next to it.

## Maintenance actions
- [ ] Maintenance branch created as `maintenance/<INDEX_NAME>+<JIRA_ID>` from the latest `functional/` version.
- [ ] Jira ticket(s) advanced to **IN PROGRESS**.
- [ ] Required change implemented in the module.
- [ ] Version number and date updated in `module.dox` **and** the checklist cover sheet.
- [ ] Config files updated in the corresponding AppModuleConfig branch — or `N/A`.
- [ ] Confirmed `functional/` has not changed since branching; if it had, the maintenance branch was **rebased** onto the latest `functional/` (rebase — not a merge commit).
- [ ] Test results and MISRA results updated in the relevant `Design/` folders.
- [ ] Basic testing performed (functional sanity check) with evidence in `Design/TestOutput/`.
- [ ] Jira ticket(s) advanced to **READY FOR REVIEW**.

---
### On merge (reviewer / automation — not gated)
- With the `functional-maintenance` label the module stays in `functional/`.
- Reviewer completes a sanity-check review and deletes the maintenance branch.
- **Reviewer sets the Jira ticket(s) to the correct state** (move them on from RESOLVED) once the merge is complete.

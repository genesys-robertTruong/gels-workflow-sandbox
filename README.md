# GeLS Workflow Sandbox

Throwaway sandbox for testing the GeLS module-workflow automation from
[GD-014-0020_GeLS_Library](https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library)
PR #4, end to end, without touching the real org repo.

Contains the same `.github/workflows/`, `.github/scripts/`, PR templates, and
`template/` module skeleton as that PR, with a minimal seed `AppModules.h/.c`
registry (real structure, two entries instead of ~180) so the scaffold/promote
scripts have something real to parse.

**One deliberate difference from production:** `module-folder-move.yml` and
`defer-module-cleanup.yml` use a plain PAT secret (`GELS_SANDBOX_PAT`) instead
of minting a GitHub App token, since standing up a second App for a disposable
test repo doesn't validate anything the real org's App setup didn't already
prove. Everything downstream of having a valid bypass-capable token is
unchanged.

Safe to delete once testing is done.
trivial change 2

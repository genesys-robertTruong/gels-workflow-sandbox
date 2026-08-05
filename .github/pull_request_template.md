<!-- gels-review-type: none -->

## Select a review type

This repository uses a different checklist for each review type, and the **merge
gate blocks this PR until a valid template + completed checklist is present**.
This default page is _not_ a valid template — pick one of the four below.

| Review type | When to use | Template |
|---|---|---|
| **IEC 62304** | New module destined for `certified/` (full GeLS dev review) | `iec62304.md` |
| **Functional** | New module destined for `functional/` (sanity review) | `functional.md` |
| **IEC 62304 – Maintenance** | Change to a released module in `certified/` | `iec62304_maintenance.md` |
| **Functional – Maintenance** | Change to a module in `functional/` | `functional_maintenance.md` |

### How to load a template

Append `&template=<file>` to the PR-creation URL, for example:

```
https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library/compare/main...<your-branch>?expand=1&template=iec62304.md
```

Quick links (replace `<your-branch>`):

- [IEC 62304](https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library/compare/main...HEAD?expand=1&template=iec62304.md)
- [Functional](https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library/compare/main...HEAD?expand=1&template=functional.md)
- [IEC 62304 – Maintenance](https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library/compare/main...HEAD?expand=1&template=iec62304_maintenance.md)
- [Functional – Maintenance](https://github.com/Genesys-Electronics-Design/GD-014-0020_GeLS_Library/compare/main...HEAD?expand=1&template=functional_maintenance.md)

> Alternatively, copy the body of the matching file from
> [`.github/PULL_REQUEST_TEMPLATE/`](.github/PULL_REQUEST_TEMPLATE) into this PR
> description (including the `<!-- gels-review-type: … -->` marker on the first line).

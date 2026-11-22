# Brightweir Triage documentation (docs-as-code demo)

A working docs-as-code pipeline: Markdown pages in Git, automated checks in GitHub Actions, API reference generated from an OpenAPI spec, and publishing through Mintlify.

**Brightweir Labs and Brightweir Triage are fictional.** This repository was built by Jason Helfenbaum ([ClicKnowledge](https://clicknowledge.com)) as a demonstration.

## What is where

| Path | What it is |
| --- | --- |
| `docs.json` | Site settings and navigation |
| `*.mdx` | Pages written by a person |
| `api-reference/openapi.yaml` | The API spec. Mintlify generates the endpoint pages from it. |
| `standards/terminology.yml` | Approved terms, enforced by the terminology check |
| `scripts/check_terminology.py` | The terminology check |
| `templates/` | Starting points for new pages (not published) |
| `.github/workflows/docs-checks.yml` | Automated checks on every pull request |
| `.github/pull_request_template.md` | Reviewer checklist |

## Preview on your computer

```bash
npm install --global mint
mint dev
```

Then open http://localhost:3000.

## How changes go live

Branch, open a pull request, let the checks pass, get one approval, merge to `main`. Mintlify publishes the merge automatically. The full process is in the **Runbook and review policy** page.

# Instructions for AI writing assistants

These instructions apply to any AI tool that drafts or edits these docs. A person reviews everything an AI tool drafts before it merges (see the **Runbook and review policy** page).

## About this project

- Documentation for Brightweir Triage, a fictional AI ticket-triage API, built as a docs-as-code demo on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML front matter. Configuration lives in `docs.json`.
- Endpoint pages are generated from `api-reference/openapi.yaml`. Never write endpoint pages by hand. Change the spec instead.

## Terminology

Follow `standards/terminology.yml`. It is enforced by `scripts/check_terminology.py`, and pull requests fail if a page breaks it.

## Style

- Plain language, second person ("you"), active voice
- Sentence case for titles and headings
- One idea per sentence
- Bold for things readers click: **Settings > API keys**
- Code format for file names, commands, fields and paths
- Start new pages from `templates/`

## Content boundaries

- Never claim the API sends replies to customers. It only drafts them for agent review.
- Mark performance figures as illustrative. Brightweir Labs is fictional.
- Do not describe or resemble any real company's product.

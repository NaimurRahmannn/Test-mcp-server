# OpenSteward MCP Test Repository

This repository is a controlled integration fixture for testing OpenSteward
against live GitHub data.

It intentionally contains:

- a repository policy in `.opensteward.yml`;
- protected security, migration, workflow, and dependency paths;
- a passing GitHub Actions check;
- architecture decision records under `docs/adr`;
- issues and historical pull requests for related-work search;
- open pull requests with low-risk, specialist, and blocked-review scenarios.

The code is a deliberately small order service so the review evidence stays
easy to inspect.

## Run tests

```shell
python -m unittest discover -s tests -v
```

## OpenSteward request

Use the actual pull request number in place of `PULL_NUMBER`:

```json
{
  "installation_id": "your install id",
  "repository": {
    "owner": "NaimurRahmannn",
    "name": "Test-mcp-server"
  },
  "pull_number": 8
}
```

## Scenario matrix

| PR | Scenario | Extra MCP input | Expected evidence |
| --- | --- | --- | --- |
| #8 | Routine documentation | none | low review cost and passing checks |
| #9 | Protected security change | `"explicit_categories": ["security"]` | security route and protected-path evidence |
| #10 | Incomplete migration draft | `"explicit_categories": ["database_migration"]` | draft, failed check, database route, and author action |
| #11 | Public API policy gaps | `"explicit_categories": ["public_api"]` | missing tests, linked issue, and approval findings |

Closed PR `#2` is an accepted idempotency implementation. Closed, unmerged PR
`#4` records the rejected Redis alternative. Together with issues `#1` and
`#3` and the ADR files, these provide related-work history.


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
  "installation_id": 148549890,
  "repository": {
    "owner": "NaimurRahmannn",
    "name": "Test-mcp-server"
  },
  "pull_number": "PULL_NUMBER"
}
```


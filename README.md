# MCP Server

This project is an MCP (Multi-Agent Conversation Protocol) Server for the given OpenAPI URL - https://api.apis.guru/v2/specs/asana.com/1.0/openapi.json, auto-generated using AG2's [MCP builder](https://mcp.ag2.ai).

## Prerequisites

*   Python 3.9+
*   pip and uv

## Installation

1.  Clone the repository:
    ```sh
    git clone <repository-url>
    cd mcp-server
    ```
2.  Install dependencies:
    The [.devcontainer/setup.sh](.devcontainer/setup.sh) script handles installing dependencies using `pip install -e ".[dev]"`. If you are not using the dev container, you can run this command manually.
    ```sh
    pip install -e ".[dev]"
    ```
    Alternatively, you can use `uv`:
    ```sh
    uv pip install --editable ".[dev]"
    ```

## Development

This project uses `ruff` for linting and formatting, `mypy` for static type checking, and `pytest` for testing.

### Linting and Formatting

To check for linting issues:
```sh
ruff check
```

To format the code:
```sh
ruff format
```
These commands are also available via the [scripts/lint.sh](scripts/lint.sh) script.

### Static Analysis

To run static analysis (mypy, bandit, semgrep):
```sh
./scripts/static-analysis.sh
```
This script is also configured as a pre-commit hook in [.pre-commit-config.yaml](.pre-commit-config.yaml).

### Running Tests

To run tests with coverage:
```sh
./scripts/test.sh
```
This will run pytest and generate a coverage report. For a combined report and cleanup, you can use:
```sh
./scripts/test-cov.sh
```

### Pre-commit Hooks

This project uses pre-commit hooks defined in [.pre-commit-config.yaml](.pre-commit-config.yaml). To install the hooks:
```sh
pre-commit install
```
The hooks will run automatically before each commit.

## Running the Server

The MCP server can be started using the [mcp_server/main.py](mcp_server/main.py) script. It supports different transport modes (e.g., `stdio`, `sse`, `streamable-http`).

To start the server (e.g., in stdio mode):
```sh
python mcp_server/main.py stdio
```

The server can be configured using environment variables:
*   `CONFIG_PATH`: Path to a JSON configuration file (e.g., [mcp_server/mcp_config.json](mcp_server/mcp_config.json)).
*   `CONFIG`: A JSON string containing the configuration.
*   `SECURITY`: Environment variables for security parameters (e.g., API keys).

Refer to the `if __name__ == "__main__":` block in [mcp_server/main.py](mcp_server/main.py) for details on how these are loaded.

The [tests/test_mcp_server.py](tests/test_mcp_server.py) file demonstrates how to start and interact with the server programmatically for testing.

## Building and Publishing

This project uses Hatch for building and publishing.
To build the project:
```sh
hatch build
```
To publish the project:
```sh
hatch publish
```
These commands are also available via the [scripts/publish.sh](scripts/publish.sh) script.

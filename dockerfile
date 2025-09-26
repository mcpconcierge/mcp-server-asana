FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY mcp_server ./mcp_server
RUN pip install uv && uv pip install --system --editable "."

ENV CONFIG_PATH=/app/mcp_server/mcp_config.json
CMD ["python", "mcp_server/main.py", "sse"]

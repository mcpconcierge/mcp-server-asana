import os
from pathlib import Path

import pytest
from autogen import AssistantAgent, LLMConfig
from autogen.mcp import create_toolkit
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def create_toolkit_and_run(session: ClientSession) -> None:
    # Create a toolkit with available MCP tools
    toolkit = await create_toolkit(session=session)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    llm_config = LLMConfig(
        api_type="openai",  # The provider
        model="gpt-4o-mini",  # The specific model
        api_key=api_key,  # Authentication
    )

    with llm_config:
        agent = AssistantAgent(name="assistant")
    # Register MCP tools with the agent
    toolkit.register_for_llm(agent)

    # Make a request using the MCP tool
    result = await agent.a_run(
        message="List all the functions that you can use",
        tools=toolkit.tools,
        max_turns=2,
        user_input=False,
    )

    await result.process()


@pytest.mark.asyncio
async def test_mcp_server() -> None:
    mcp_server_path = Path("./mcp_server")  # Path to the MCP server directory
    server_params = StdioServerParameters(
        # add security parameters here as env var
        command="python",  # The command to run the server
        args=[
            str(mcp_server_path / "main.py"),  # Path to the server script
            "stdio",
        ],  # Path to server script and transport mode
        env={
            "CONFIG_PATH": str(
                mcp_server_path.absolute() / "mcp_config.json"
            ),  # Path to the config file, check the generated files as the names change with each generation
        },
        # env={
        #     "SECURITY": str(security.dump()),
        # },
    )

    async with (
        stdio_client(server_params) as (read, write),
        ClientSession(read, write) as session,
    ):
        # Initialize the connection
        await session.initialize()
        await create_toolkit_and_run(session)

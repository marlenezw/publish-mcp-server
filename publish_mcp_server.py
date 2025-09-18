from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("publish_mcp_server")

@mcp.prompt(name="publish_mcp_server_prompt", 
            description="Prompt for an agent to publish an MCP server to the MCP Registry")
def publish_mcp_server_prompt(server_name: str) -> str:
    """Publish and MCP Sever to the MCP Registry"""

    prompt = f"""Read https://raw.githubusercontent.com/modelcontextprotocol/registry/refs/heads/main/docs/guides/publishing/publish-server.md 
    and https://raw.githubusercontent.com/modelcontextprotocol/registry/refs/heads/main/docs/guides/publishing/github-actions.md. 
    Evaluate the best way to publish the {server_name} server to the registry (prefer automated CI flows over manual flows where possible), 
    and implement that. If possible, validate the server.json against the $schema before telling the user you are done, using a proper 
    json schema library or tool available on the user's machine. If you get stuck, guide the user through the parts of the publishing process 
    they need to do (e.g. logging into the publisher CLI if doing manual pubishing).
    """
    return prompt

def main():
    """Main entry point for the server."""
    mcp.run()

if __name__ == "__main__":
    main()
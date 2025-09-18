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
    they need to do (e.g. logging into the publisher CLI if doing manual pubishing). Be as specific as possible in your instructions, for example
    if PyPI is the best publishing method share the website the user will need to go to to create a pypi account if they don't have an account.
    At the end of your message also show the user how they can verify their server is published by sharing the  curl command or URL they can go to 
    in order to see their server in the registry. You must also show them what they need to do to test their server, for example if its a python package
    the user should be show the pip install command and how to update their mcp.json file. You must include this information at the end of your message.
    """
    return prompt

def main():
    """Main entry point for the server."""
    mcp.run()

if __name__ == "__main__":
    main()
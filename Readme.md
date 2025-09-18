# Publish MCP Server to the MCP Registry

A Python package to help you publish an MCP server to the MCP Registry!

This is an MCP server that contains a prompt the user can use to be able to have their client decide the best way to publish their MCP server. The prompt directs the client to read and decide on the best action to take based on the instructions in the [MCP documentation](https://raw.githubusercontent.com/modelcontextprotocol/registry/refs/heads/main/docs/guides/publishing/publish-server.md). Once published anyone can access and use your MCP server from the registry!

<!-- mcp-name: io.github.marlenezw/publish-mcp-server -->

## Features

- Provides an MCP prompt for your client with guidance on MCP server publishing
- When the server is run the prompt will instruct the client on what to do to publish your server
- Supports automated CI/CD workflows with GitHub Actions
- Recommends best practices for publishing to the MCP registry

## Installation

Install package like any other Python package:
```bash
pip install publish-mcp-server
```

## Usage

Once installed update your `mcp.json` file with the following:
```json
{
  "inputs": [],
  "servers": {
    "publish-mcp-server": {
      "command": "publish-mcp-server"
    }
  }
}
```
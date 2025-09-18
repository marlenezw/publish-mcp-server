"""Publish MCP Server - A tool to help publish MCP servers to the registry."""

__version__ = "0.1.1"
__author__ = "Marlene Mhangami"
__email__ = "marlenemhangami@gmail.com"

from .publish_mcp_server import mcp, main

__all__ = ["mcp", "main"]
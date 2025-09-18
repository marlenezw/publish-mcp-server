#!/usr/bin/env python3
"""Validate server.json against the MCP server schema."""

import json
import requests
from jsonschema import validate, ValidationError
import sys

def validate_server_json():
    """Validate the server.json file against the MCP server schema."""
    
    # Read the server.json file
    try:
        with open('server.json', 'r') as f:
            server_config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: server.json file not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in server.json: {e}")
        return False
    
    # Get the schema URL from the server.json
    schema_url = server_config.get('$schema')
    if not schema_url:
        print("❌ Error: No $schema field found in server.json")
        return False
    
    print(f"📋 Fetching schema from: {schema_url}")
    
    # Fetch the schema
    try:
        response = requests.get(schema_url)
        response.raise_for_status()
        schema = response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching schema: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing schema JSON: {e}")
        return False
    
    # Validate the server.json against the schema
    try:
        validate(instance=server_config, schema=schema)
        print("✅ server.json is valid according to the MCP server schema!")
        return True
    except ValidationError as e:
        print(f"❌ Validation error: {e.message}")
        print(f"   Failed at path: {' -> '.join(str(p) for p in e.path)}")
        return False

if __name__ == "__main__":
    if validate_server_json():
        sys.exit(0)
    else:
        sys.exit(1)
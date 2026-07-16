"""Publish MCP metadata to a discovery registry.

Usage:
  export MCP_REGISTRY_URL=https://example.com/register
  export MCP_REGISTRY_TOKEN=...   # optional
  python -m app.mcp_publish

The script fetches local MCP metadata (http://localhost:9000/mcp/metadata)
and POSTs it to MCP_REGISTRY_URL as JSON. The exact registry contract may vary;
this script uses a generic /register endpoint and includes an Authorization
bearer token if MCP_REGISTRY_TOKEN is set.
"""
from __future__ import annotations
import os
import sys
import json
import httpx

MCP_LOCAL = os.environ.get("MCP_LOCAL_URL", "http://localhost:9000/mcp/metadata")
REGISTRY = os.environ.get("MCP_REGISTRY_URL")
TOKEN = os.environ.get("MCP_REGISTRY_TOKEN")

if not REGISTRY:
    print("MCP_REGISTRY_URL not set. Export MCP_REGISTRY_URL and try again.")
    sys.exit(2)


def fetch_metadata(local_url: str) -> dict:
    r = httpx.get(local_url, timeout=10.0)
    r.raise_for_status()
    return r.json()


def publish(metadata: dict, registry_url: str, token: str | None = None) -> dict:
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    # Expect registry to accept POST to provided URL
    r = httpx.post(registry_url, json=metadata, headers=headers, timeout=10.0)
    r.raise_for_status()
    return r.json()


def main():
    print(f"Fetching local MCP metadata from {MCP_LOCAL}")
    md = fetch_metadata(MCP_LOCAL)
    print("Metadata fetched. Publishing to registry:", REGISTRY)
    resp = publish(md, REGISTRY, TOKEN)
    print("Publish response:")
    print(json.dumps(resp, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

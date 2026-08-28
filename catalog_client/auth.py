"""Auth helper patched in by scripts/patch_python_client.py.

openapi-generator's Configuration.access_token / auth_settings() does not reliably
attach the Authorization header to outgoing requests. set_default_header is honored
on every request, so we use that instead.
"""
from __future__ import annotations

import os

from catalog_client.api_client import ApiClient
from catalog_client.configuration import Configuration


def authenticated_client(base_url: str | None = None, token: str | None = None) -> ApiClient:
    token = token or os.environ.get("CATALOG_API_TOKEN")
    if not token:
        raise RuntimeError("Set CATALOG_API_TOKEN env var (or pass token=) to authenticate.")
    config = Configuration(host=base_url or os.environ.get("CATALOG_API_BASE_URL", "http://localhost:8080"))
    client = ApiClient(config)
    client.set_default_header("Authorization", f"Bearer {token}")
    return client

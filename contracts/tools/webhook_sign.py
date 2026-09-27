"""HMAC-SHA256 signing for outcome webhooks. Header: X-Ashley-Signature: sha256=<hex>.

The signed message is the timestamp header value, a dot, and the raw request body:
    message = f"{timestamp}.".encode() + body
"""
from __future__ import annotations

import hashlib
import hmac

PREFIX = "sha256="


def sign(secret: bytes, message: bytes) -> str:
    return PREFIX + hmac.new(secret, message, hashlib.sha256).hexdigest()


def verify(secret: bytes, message: bytes, header_value: str) -> bool:
    if not isinstance(header_value, str):
        return False
    if not header_value.isascii():
        return False
    if not header_value.startswith(PREFIX):
        return False
    return hmac.compare_digest(sign(secret, message), header_value)

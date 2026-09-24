"""Canonical content hash for instruments. Text changes must change the hash; status changes must not."""
from __future__ import annotations

import hashlib
import json

HASH_EXCLUDED = ("content_hash", "status")


def canonical_hash(instrument: dict) -> str:
    body = {key: value for key, value in instrument.items() if key not in HASH_EXCLUDED}
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_hash(instrument: dict) -> bool:
    return instrument.get("content_hash") == canonical_hash(instrument)

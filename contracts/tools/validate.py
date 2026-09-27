"""Validate JSON documents against the contract schemas in contracts/schemas."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "contracts" / "schemas"
FIXTURES = ROOT / "contracts" / "fixtures"
INSTRUMENTS = ROOT / "contracts" / "instruments"


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def load_schema(name: str) -> dict:
    return load_json(SCHEMAS / f"{name}.schema.json")


def errors_for(schema_name: str, doc: dict) -> list[str]:
    """Return sorted validation messages; an empty list means the document is valid."""
    validator = Draft202012Validator(load_schema(schema_name))
    return sorted(error.message for error in validator.iter_errors(doc))


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: validate.py <schema-name> <document.json>", file=sys.stderr)
        return 2
    try:
        errors = errors_for(argv[1], load_json(Path(argv[2])))
    except (OSError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    for message in errors:
        print(message)
    print("VALID" if not errors else f"INVALID ({len(errors)} errors)")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

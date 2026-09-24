import re

from contracts.tools.validate import SCHEMAS, load_json

FORBIDDEN = re.compile(r"(expression|emotion|facial|\bface\b|appearance|accent|gaze|posture|smile|attractive)", re.IGNORECASE)


def _property_names(node, found: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "properties" and isinstance(value, dict):
                for prop_name, prop_schema in value.items():
                    found.add(prop_name)
                    _property_names(prop_schema, found)
            elif key in ("enum", "required", "const", "pattern", "description", "title"):
                continue
            else:
                _property_names(value, found)
    elif isinstance(node, list):
        for item in node:
            _property_names(item, found)


def test_no_schema_exposes_appearance_or_emotion_features():
    offenders = []
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        names: set[str] = set()
        _property_names(load_json(schema_path), names)
        offenders += [f"{schema_path.name}:{name}" for name in sorted(names) if FORBIDDEN.search(name)]
    assert offenders == []


def test_guard_catches_a_forbidden_name():
    names: set[str] = set()
    _property_names({"properties": {"facial_expression_score": {"type": "number"}}}, names)
    assert any(FORBIDDEN.search(name) for name in names)

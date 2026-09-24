import pytest

from contracts.tools.validate import FIXTURES, INSTRUMENTS, SCHEMAS, errors_for, load_json


def _cases(kind: str) -> list[tuple[str, object]]:
    root = FIXTURES / kind
    return sorted(
        (schema_dir.name, path)
        for schema_dir in root.iterdir() if schema_dir.is_dir()
        for path in schema_dir.glob("*.json")
    )


VALID = _cases("valid")
INVALID = _cases("invalid")


@pytest.mark.parametrize("schema_name,path", VALID, ids=[f"{name}/{path.name}" for name, path in VALID])
def test_valid_fixture_validates(schema_name, path):
    assert errors_for(schema_name, load_json(path)) == []


@pytest.mark.parametrize("schema_name,path", INVALID, ids=[f"{name}/{path.name}" for name, path in INVALID])
def test_invalid_fixture_fails(schema_name, path):
    assert errors_for(schema_name, load_json(path)) != []


def test_every_instrument_file_validates():
    files = sorted(INSTRUMENTS.glob("*.json"))
    assert files, "no instruments found"
    for path in files:
        assert errors_for("instrument", load_json(path)) == [], path.name


def test_every_schema_has_valid_and_invalid_examples():
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        name = schema_path.name.removesuffix(".schema.json")
        has_valid = any((FIXTURES / "valid" / name).glob("*.json")) or (name == "instrument" and any(INSTRUMENTS.glob("*.json")))
        has_invalid = any((FIXTURES / "invalid" / name).glob("*.json"))
        assert has_valid, f"{name}: no valid example"
        assert has_invalid, f"{name}: no invalid example"

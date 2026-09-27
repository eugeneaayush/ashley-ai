import re

import pytest

from contracts.tools.validate import SCHEMAS, load_json

FORBIDDEN_TOKENS = {
    "expression", "expressions", "emotion", "emotions", "emotional", "face", "faces", "facial",
    "appearance", "accent", "accents", "gaze", "posture", "smile", "smiles", "smiling",
    "attractive", "attractiveness", "tone", "prosody", "pitch", "eye", "eyes", "affect",
}
SKIPPED_KEYS = ("required", "pattern", "description", "title")
SEPARATORS = re.compile(r"[_\-.\s]+")
CAMEL_BOUNDARY = re.compile(r"(?<=[a-z])(?=[A-Z])")


def tokens(name: str) -> set[str]:
    """Lowercase word tokens: split on `_`, `-`, `.`, whitespace, and lower-to-upper boundaries."""
    words: set[str] = set()
    for part in SEPARATORS.split(name):
        for word in CAMEL_BOUNDARY.split(part):
            if word:
                words.add(word.lower())
    return words


def forbidden_tokens(name: str) -> set[str]:
    return tokens(name) & FORBIDDEN_TOKENS


def _names(node, found: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "properties" and isinstance(value, dict):
                for prop_name, prop_schema in value.items():
                    found.add(prop_name)
                    _names(prop_schema, found)
            elif key == "enum" and isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        found.add(item)
            elif key == "const" and isinstance(value, str):
                found.add(value)
            elif key in SKIPPED_KEYS:
                continue
            else:
                _names(value, found)
    elif isinstance(node, list):
        for item in node:
            _names(item, found)


def test_no_schema_exposes_appearance_or_emotion_features():
    offenders = []
    for schema_path in sorted(SCHEMAS.glob("*.schema.json")):
        names: set[str] = set()
        _names(load_json(schema_path), names)
        offenders += [
            f"{schema_path.name}:{name}" for name in sorted(names) if forbidden_tokens(name)
        ]
    assert offenders == []


@pytest.mark.parametrize(
    "name",
    ["face_score", "faceScore", "facial_expression", "voice_tone", "eye_contact", "smileRate"],
)
def test_guard_flags_forbidden_names(name):
    assert forbidden_tokens(name)


@pytest.mark.parametrize(
    "name", ["interface_id", "surface_area", "pitchfork_count", "retail-associate"]
)
def test_guard_allows_names_whose_words_only_overlap(name):
    assert forbidden_tokens(name) == set()


def test_guard_flags_forbidden_enum_value():
    names: set[str] = set()
    _names({"enum": ["retail-associate", "facial-expression"]}, names)
    assert [name for name in sorted(names) if forbidden_tokens(name)] == ["facial-expression"]


def test_guard_skips_description_and_pattern_text():
    names: set[str] = set()
    _names({"description": "measures facial expression", "pattern": "^face_[0-9]+$"}, names)
    assert names == set()

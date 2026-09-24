from contracts.tools.validate import main


def test_usage_error_returns_2(capsys):
    assert main(["validate.py"]) == 2
    assert "usage" in capsys.readouterr().err


def test_draft_2020_12_validator_is_available():
    from jsonschema import Draft202012Validator

    validator = Draft202012Validator({"type": "integer"})
    assert sorted(e.message for e in validator.iter_errors("x")) == ["'x' is not of type 'integer'"]

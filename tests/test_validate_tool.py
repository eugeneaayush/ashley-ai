from contracts.tools.validate import errors_for, main


def test_usage_error_returns_2(capsys):
    assert main(["validate.py"]) == 2
    assert "usage" in capsys.readouterr().err


def test_missing_document_returns_2(capsys):
    assert main(["validate.py", "interview_session", "no/such/document.json"]) == 2
    captured = capsys.readouterr()
    assert "error:" in captured.err
    assert "VALID" not in captured.out


def test_non_object_document_reports_a_type_error():
    errors = errors_for("interview_session", [1, 2])
    assert any("is not of type 'object'" in message for message in errors), errors

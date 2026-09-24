from contracts.tools.validate import ROOT, SCHEMAS

README = ROOT / "contracts" / "README.md"


def test_readme_names_every_schema_and_the_webhook_doc():
    text = README.read_text(encoding="utf-8")
    for schema_path in SCHEMAS.glob("*.schema.json"):
        assert schema_path.name in text, schema_path.name
    assert "WEBHOOKS.md" in text
    assert "content_hash" in text

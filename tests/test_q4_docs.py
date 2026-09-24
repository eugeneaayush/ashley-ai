from contracts.tools.validate import ROOT

DOCS = ROOT / "docs" / "moat"
ATS_SYSTEMS = ["Workstream", "Fountain", "Harri", "Ashby", "Greenhouse", "iCIMS", "Bullhorn"]
FLAGSHIP_COLUMNS = ["Company", "Segment", "Locations", "Applicants/month", "ATS", "Contact path", "Why now", "Status", "Next step"]


def test_flagship_doc_has_criteria_and_tracking_columns():
    text = (DOCS / "flagship-targets.md").read_text(encoding="utf-8")
    assert "## Qualification criteria" in text
    assert "## Disqualifiers" in text
    assert "## Definition of done" in text
    for column in FLAGSHIP_COLUMNS:
        assert column in text, column


def test_ats_check_covers_every_candidate_system():
    text = (DOCS / "ats-check.md").read_text(encoding="utf-8")
    for system in ATS_SYSTEMS:
        assert f"## {system}" in text, system
    assert "Webhook on stage change" in text
    assert "Write back a score" in text


AUDIT_VENDORS = ["BABL AI", "Warden AI", "Holistic AI"]
ISO_SECTIONS = ["## 4. Context", "## 5. Leadership", "## 6. Planning", "## 7. Support", "## 8. Operation", "## 9. Performance evaluation", "## 10. Improvement"]


def test_audit_rfq_names_vendors_and_questions():
    text = (DOCS / "audit-vendor-rfq.md").read_text(encoding="utf-8")
    for vendor in AUDIT_VENDORS:
        assert vendor in text, vendor
    assert "## Questions for every vendor" in text
    assert "impact ratio" in text
    assert "publication" in text.lower()


def test_iso42001_skeleton_maps_clauses_to_evidence():
    text = (DOCS / "iso42001-skeleton.md").read_text(encoding="utf-8")
    for section in ISO_SECTIONS:
        assert section in text, section
    for evidence in ["instrument.schema.json", "disclosure_receipt.schema.json", "audit_export.schema.json"]:
        assert evidence in text, evidence

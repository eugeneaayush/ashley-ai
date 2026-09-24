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

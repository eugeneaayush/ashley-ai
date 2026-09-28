from contracts.tools.validate import ROOT

WIKI = ROOT / "blueprint" / "wiki" / "moat-decisions.md"
INDEX = ROOT / "blueprint" / "INDEX.md"
SPEC = "docs/superpowers/specs/2026-09-23-competitive-moat-design.md"


def test_wiki_page_links_spec_and_contracts():
    text = WIKI.read_text(encoding="utf-8")
    assert SPEC in text
    assert "contracts/schemas" in text
    assert "words only" in text.lower()


def test_index_lists_wiki_page():
    assert "wiki/moat-decisions.md" in INDEX.read_text(encoding="utf-8")


def test_every_routed_skill_file_exists():
    import re

    claude_md = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    routed = re.findall(r"\|\s*(gtm-skills/[\w-]+\.md)\b", claude_md)
    assert "gtm-skills/pilot-follow-up.md" in routed
    missing = [path for path in routed if not (ROOT / path).is_file()]
    assert missing == []

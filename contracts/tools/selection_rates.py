"""Selection rates and impact ratios per group, in the four-fifths form used by adverse-impact reporting.

Input rows: one per candidate per category, {"category": str, "group": str, "selected": bool}.
"selected" means an application_decision event with decision == "advanced".
"""
from __future__ import annotations

FOUR_FIFTHS = 0.8


def impact_ratios(rows: list[dict]) -> list[dict]:
    counts: dict[tuple[str, str], list[int]] = {}
    for row in rows:
        key = (row["category"], row["group"])
        applicants_selected = counts.setdefault(key, [0, 0])
        applicants_selected[0] += 1
        applicants_selected[1] += 1 if row["selected"] else 0

    by_category: dict[str, dict[str, list[int]]] = {}
    for (category, group), applicants_selected in counts.items():
        by_category.setdefault(category, {})[group] = applicants_selected

    output: list[dict] = []
    for category in sorted(by_category):
        groups = by_category[category]
        rates = {group: (selected / applicants if applicants else 0.0) for group, (applicants, selected) in groups.items()}
        top = max(rates.values())
        for group in sorted(groups):
            applicants, selected = groups[group]
            ratio = rates[group] / top if top else 0.0
            output.append({
                "category": category,
                "group": group,
                "applicants": applicants,
                "selected": selected,
                "selection_rate": round(rates[group], 4),
                "impact_ratio": round(ratio, 4),
                "flagged": (ratio < FOUR_FIFTHS) if top else False,
            })
    return output

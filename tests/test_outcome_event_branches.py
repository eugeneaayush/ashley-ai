from contracts.tools.validate import load_schema


def _payload_rules_for(schema: dict, event_type: str) -> int:
    count = 0
    for branch in schema["allOf"]:
        condition = branch["if"]["properties"]["event_type"]
        if condition.get("const") == event_type or event_type in condition.get("enum", []):
            count += 1
    return count


def test_every_event_type_has_exactly_one_payload_rule():
    schema = load_schema("outcome_event")
    for event_type in schema["properties"]["event_type"]["enum"]:
        assert _payload_rules_for(schema, event_type) == 1, event_type

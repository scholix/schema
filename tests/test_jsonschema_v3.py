"""Test example JSON document against the JSONSchema."""
from jsonschema import validate


def test_json_example(json_schema_v3, json_example_v3):
    """Test simple relation event JSONSchema validation."""
    # Will rase in case of schema validation errors
    validate(json_example_v3, json_schema_v3)

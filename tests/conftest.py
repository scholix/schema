"""Tests configuration."""
import pytest
import os
import json

@pytest.fixture
def test_dir():
    """Test directory."""
    return os.path.dirname(__file__)


@pytest.fixture
def data_dir(test_dir):
    """Test data directory."""
    return os.path.join(test_dir, 'data')


@pytest.fixture
def jsonschema_dir(test_dir):
    """JSON schemas directory."""
    return os.path.join(test_dir, '..', 'json')


def load_json_schema(basedir, filename):
    """Helper function for loading JSON schemas."""
    with open(os.path.join(basedir, filename)) as fp:
        schema = json.load(fp)
    return schema


@pytest.fixture
def json_schema_v3(jsonschema_dir):
    """Scholix JSON Schema v3."""
    return load_json_schema(os.path.join(jsonschema_dir, 'v3'), 'schema.json')


@pytest.fixture
def json_example_v3(jsonschema_dir):
    """Example of JSON under Scholix JSON Schema v3."""
    return load_json_schema(os.path.join(jsonschema_dir, 'v3', 'example'),
                            'example.json')

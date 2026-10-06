from pathlib import Path

import pytest

from specrift.loader import SpecLoadError, load_spec

FIXTURES = Path(__file__).parent / "fixtures"


def test_load_valid_spec():
    spec = load_spec(FIXTURES / "weather_v1.yaml")
    assert "/weather/{city}" in spec["paths"]


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_spec(FIXTURES / "does_not_exit.yaml")


def test_invalid_spec_raises():
    with pytest.raises(SpecLoadError):
        load_spec(FIXTURES / "invalid.yaml")


def test_empty_file_raises():
    with pytest.raises(SpecLoadError):
        load_spec(FIXTURES / "empty.yaml")

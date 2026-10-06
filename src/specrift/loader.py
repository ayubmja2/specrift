"""
3. Write the loader in src/specrift/loader.py. Your goal is a function that:

takes a file path
reads the YAML into a dict
validates it with openapi-spec-validator
raises a clear error if the file is missing or the spec is invalid
returns the dict

4. Write tests in tests/test_loader.py:

loading weather_v1.yaml returns a dict containing /weather/{city} under paths
loading a file that doesn't exist raises an error
loading an invalid spec raises an error (create a broken invalid.yaml fixture, e.g. missing the openapi line)
"""

from typing import Any 
from pathlib import Path 
import yaml
from openapi_spec_validator import validate_spec



def load_spec(file_path:str) -> dict[str, Any]:
    # Load and validate an openapi yaml spec

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"OpenApi spec file is not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            spec = yaml.safe_load(file)
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid Yaml in openapi spec '{path}': {error}") from error

    try:
        validate_spec(spec)
    except Exception as error:
        raise ValueError(f"OpenAPI spec validation failed for '{path}': {error}") from error

    return spec

    
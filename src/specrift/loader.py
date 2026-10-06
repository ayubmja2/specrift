from pathlib import Path
from typing import Any

import yaml
from openapi_spec_validator import validate
from openapi_spec_validator.validation.exceptions import (
    OpenAPIValidationError,
    ValidatorDetectError,
)


class SpecLoadError(Exception):
    """Raised when an openapi spec can't be read or is invalid."""


def load_spec(file_path: str) -> dict[str, Any]:
    # Load and validate an openapi yaml spec

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"OpenApi spec file is not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            spec = yaml.safe_load(file)
    except yaml.YAMLError as error:
        raise SpecLoadError(
            f"Invalid Yaml in openapi spec '{path}': {error}"
        ) from error

    if not isinstance(spec, dict):
        raise SpecLoadError(f"'{path}' does not contain a yaml mapping")

    try:
        validate(spec)
    except (OpenAPIValidationError, ValidatorDetectError) as error:
        raise SpecLoadError(
            f"OpenAPI spec validation failed for '{path}': {error}"
        ) from error

    return spec

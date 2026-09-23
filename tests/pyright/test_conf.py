from .base import run_pyright


def test_settings_constants() -> None:
    results = run_pyright(
        """\
from typing import Literal
from typing_extensions import assert_type
from django.conf import (
    DEFAULT_STORAGE_ALIAS,
    ENVIRONMENT_VARIABLE,
    STATICFILES_STORAGE_ALIAS,
)

assert_type(ENVIRONMENT_VARIABLE, Literal["DJANGO_SETTINGS_MODULE"])
assert_type(DEFAULT_STORAGE_ALIAS, Literal["default"])
assert_type(STATICFILES_STORAGE_ALIAS, Literal["staticfiles"])
reveal_type(DEFAULT_STORAGE_ALIAS)
"""
    )
    assert [r for r in results if r.type == "error"] == []
    assert results, "The type checker must report the requested revealed types"

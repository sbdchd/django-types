from .base import run_pyright


def test_async_test_client_is_importable() -> None:
    """An async test suite imports AsyncClient from django.test, as the docs show."""
    results = run_pyright(
        """\
from django.test import AsyncClient, AsyncRequestFactory

reveal_type(AsyncClient)
reveal_type(AsyncRequestFactory)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_http_response_base_is_importable() -> None:
    """Middleware and view code annotates against HttpResponseBase."""
    results = run_pyright(
        """\
from django.http import HttpResponseBase

def handler() -> HttpResponseBase: ...
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_capture_on_commit_callbacks() -> None:
    """A test asserts on work deferred with transaction.on_commit."""
    results = run_pyright(
        """\
from django.test import TestCase

class Foo(TestCase):
    def test_it(self) -> None:
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            reveal_type(callbacks)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_storage_handler_is_importable() -> None:
    """Code reads a non-default storage backend by its STORAGES alias."""
    results = run_pyright(
        """\
from django.core.files.storage import InvalidStorageError, Storage, storages

def get(alias: str) -> Storage:
    try:
        return storages[alias]
    except InvalidStorageError:
        raise
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_parse_header_parameters_is_importable() -> None:
    """A request handler splits a Content-Type header into its value and params."""
    results = run_pyright(
        """\
from django.utils.http import parse_header_parameters

value, params = parse_header_parameters("text/html; charset=utf-8", max_length=4096)
reveal_type(value)
reveal_type(params)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_admin_site_get_model_admin() -> None:
    """A test asserts which bulk actions a model's admin exposes."""
    results = run_pyright(
        """\
from django.contrib.admin.sites import site
from django.contrib.auth.models import User

model_admin = site.get_model_admin(User)
reveal_type(model_admin)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_http_response_supports_in() -> None:
    """A test asserts a header is present with `in`, the way Django documents it."""
    results = run_pyright(
        """\
from django.http import HttpResponse

response = HttpResponse()
reveal_type("Retry-After" in response)
"""
    )
    assert [r for r in results if r.type == "error"] == []

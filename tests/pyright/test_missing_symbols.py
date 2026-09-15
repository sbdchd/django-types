from .base import run_pyright


def test_async_test_client_is_importable() -> None:
    """An async test suite imports AsyncClient from django.test, as the docs show.

    Both AsyncClient and AsyncRequestFactory are defined in django/test/client.pyi
    but were never re-exported from the package, so the import itself was rejected
    and every annotation using them degraded to Unknown.
    """
    results = run_pyright(
        """\
from django.test import AsyncClient, AsyncRequestFactory

reveal_type(AsyncClient)
reveal_type(AsyncRequestFactory)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_http_response_base_is_importable() -> None:
    """Middleware and view code annotates against HttpResponseBase.

    It is the common base of HttpResponse and StreamingHttpResponse, so it is the
    honest annotation for anything that may return either. It is defined in
    http/response.pyi but was not re-exported from django.http, which is where
    Django's own docs import it from.
    """
    results = run_pyright(
        """\
from django.http import HttpResponseBase

def handler() -> HttpResponseBase: ...
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_capture_on_commit_callbacks() -> None:
    """A test asserts on work deferred with transaction.on_commit.

    TestCase wraps each test in a transaction that never commits, so on_commit
    callbacks never fire; captureOnCommitCallbacks(execute=True) is the documented
    way to run them. It has existed since Django 3.2 and was absent from the stub.
    """
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
    """Code reads a non-default storage backend by its STORAGES alias.

    Django 4.2 replaced get_storage_class with the storages registry, so
    storages["uploads"] is now the supported way to reach a configured backend,
    and InvalidStorageError is what it raises for an unknown alias. Neither was
    in the stub.
    """
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
    """A request handler splits a Content-Type header into its value and params.

    parse_header_parameters is Django's public helper for this - it is what
    Django's own multipart parser and FileResponse use - and it was missing from
    the django.utils.http stub.
    """
    results = run_pyright(
        """\
from django.utils.http import parse_header_parameters

value, params = parse_header_parameters("text/html; charset=utf-8")
reveal_type(value)
reveal_type(params)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_admin_site_get_model_admin() -> None:
    """A test asserts which bulk actions a model's admin exposes.

    AdminSite.get_model_admin is the supported way to reach a registered
    ModelAdmin - Django added it in 5.0 precisely so callers stop reading the
    private _registry dict - but the stub only declared is_registered, so the
    lookup failed to resolve at all.
    """
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
    """A test asserts a header is present with `in`, the way Django documents it.

    HttpResponseBase aliases __contains__ to has_header, so `"Retry-After" in
    response` is the idiomatic spelling. The stub declared only has_header, so
    the `in` form was rejected and call sites had to be rewritten around it.
    """
    results = run_pyright(
        """\
from django.http import HttpResponse

response = HttpResponse()
reveal_type("Retry-After" in response)
"""
    )
    assert [r for r in results if r.type == "error"] == []

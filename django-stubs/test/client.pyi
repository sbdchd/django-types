from collections.abc import Mapping
from io import BytesIO
from json import JSONEncoder
from re import Pattern
from types import TracebackType
from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.http.cookie import SimpleCookie
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBase

BOUNDARY: str = ...
MULTIPART_CONTENT: str = ...
CONTENT_TYPE_RE: Pattern[str] = ...
JSON_CONTENT_TYPE_RE: Pattern[str] = ...

class RedirectCycleError(Exception):
    last_response: HttpResponseBase = ...
    redirect_chain: list[tuple[str, int]] = ...
    def __init__(self, message: str, last_response: HttpResponseBase) -> None: ...

class FakePayload:
    read_started: bool = ...
    def __init__(self, content: bytes | str | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def read(self, num_bytes: int = ...) -> bytes: ...
    def write(self, content: bytes | str) -> None: ...

class ClientHandler(BaseHandler):
    enforce_csrf_checks: bool = ...
    def __init__(
        self, enforce_csrf_checks: bool = ..., *args: Any, **kwargs: Any
    ) -> None: ...
    def __call__(self, environ: dict[str, Any]) -> HttpResponseBase: ...

class AsyncClientHandler(BaseHandler):
    enforce_csrf_checks: bool = ...
    def __init__(
        self, enforce_csrf_checks: bool = ..., *args: Any, **kwargs: Any
    ) -> None: ...
    async def __call__(self, scope: dict[str, Any]) -> HttpResponseBase: ...

def encode_multipart(boundary: str, data: dict[str, Any]) -> bytes: ...
def encode_file(boundary: str, key: str, file: Any) -> list[bytes]: ...

_RequestData = Any | None

class RequestFactory:
    json_encoder: type[JSONEncoder]
    defaults: dict[str, str]
    cookies: SimpleCookie  # type: ignore [type-arg]
    errors: BytesIO
    def __init__(
        self,
        *,
        json_encoder: type[JSONEncoder] = ...,
        headers: Mapping[str, Any] | None = ...,
        **defaults: Any,
    ) -> None: ...
    def request(self, **request: Any) -> WSGIRequest: ...
    def get(
        self,
        path: str,
        data: _RequestData = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def post(
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def head(
        self,
        path: str,
        data: _RequestData = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def trace(
        self,
        path: str,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def options(
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def put(
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def patch(
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def delete(
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def generic(
        self,
        method: str,
        path: str,
        data: _RequestData = ...,
        content_type: str | None = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...

class Client(RequestFactory):
    handler: ClientHandler
    raise_request_exception: bool
    exc_info: tuple[type[BaseException], BaseException, TracebackType] | None
    headers: dict[str, Any]
    def __init__(
        self,
        enforce_csrf_checks: bool = ...,
        raise_request_exception: bool = ...,
        *,
        json_encoder: type[JSONEncoder] = ...,
        headers: Mapping[str, Any] | None = ...,
        **defaults: Any,
    ) -> None: ...
    # Silence type warnings, since this class overrides arguments and return types in an unsafe manner.
    def request(self, **request: Any) -> HttpResponse: ...  # type: ignore [override]
    def get(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def head(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def trace(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def store_exc_info(self, **kwargs: Any) -> None: ...
    @property
    def session(self) -> SessionBase: ...
    def login(self, **credentials: Any) -> bool: ...
    def force_login(
        self, user: AbstractBaseUser, backend: str | None = ...
    ) -> None: ...
    def logout(self) -> None: ...

class AsyncRequestFactory(RequestFactory): ...

class AsyncClient(AsyncRequestFactory):
    handler: AsyncClientHandler
    raise_request_exception: bool
    exc_info: tuple[type[BaseException], BaseException, TracebackType] | None
    headers: dict[str, Any]
    def __init__(
        self,
        enforce_csrf_checks: bool = ...,
        raise_request_exception: bool = ...,
        *,
        json_encoder: type[JSONEncoder] = ...,
        headers: Mapping[str, Any] | None = ...,
        **defaults: Any,
    ) -> None: ...
    # Silence type warnings, since this class overrides arguments and return types in an unsafe manner.
    async def request(self, **request: Any) -> HttpResponse: ...  # type: ignore [override]
    async def get(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def post(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def head(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def trace(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def options(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def put(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def patch(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def delete(  # type: ignore [override]
        self,
        path: str,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        QUERY_STRING: str = ...,
        headers: Mapping[str, Any] | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def store_exc_info(self, **kwargs: Any) -> None: ...
    @property
    def session(self) -> SessionBase: ...
    def login(self, **credentials: Any) -> bool: ...
    def force_login(
        self, user: AbstractBaseUser, backend: str | None = ...
    ) -> None: ...
    def logout(self) -> None: ...

def conditional_content_removal(
    request: HttpRequest, response: HttpResponseBase
) -> HttpResponse: ...

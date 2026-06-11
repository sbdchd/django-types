from collections.abc import AsyncGenerator, Callable, Generator, Iterable, Mapping
from http import HTTPStatus
from io import BytesIO, IOBase
from json import JSONEncoder
from re import Pattern
from types import TracebackType
from typing import Any, TypeAlias, TypeVar

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.http.cookie import SimpleCookie
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBase
from django.utils.functional import _StrOrPromise

_T = TypeVar("_T")

BOUNDARY: str
MULTIPART_CONTENT: str
CONTENT_TYPE_RE: Pattern[str]
JSON_CONTENT_TYPE_RE: Pattern[str]
REDIRECT_STATUS_CODES: frozenset[HTTPStatus]

class RedirectCycleError(Exception):
    last_response: HttpResponseBase
    redirect_chain: list[tuple[str, int]]
    def __init__(self, message: str, last_response: HttpResponseBase) -> None: ...

class FakePayload(IOBase):
    read_started: bool
    def __init__(self, content: bytes | str | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def read(self, size: int = ..., /) -> bytes: ...
    def readline(self, size: int | None = ..., /) -> bytes: ...
    def write(self, b: bytes | str, /) -> None: ...

def closing_iterator_wrapper(iterable: Iterable[_T], close: Callable) -> Generator[_T]: ...
async def aclosing_iterator_wrapper(iterable: Iterable[_T], close: Callable) -> AsyncGenerator[_T]: ...

_Response = TypeVar("_Response", bound=HttpResponse)

def conditional_content_removal(request: HttpRequest, response: _Response) -> _Response: ...

class ClientHandler(BaseHandler):
    enforce_csrf_checks: bool = ...
    def __init__(self, enforce_csrf_checks: bool = ..., *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, environ: dict[str, Any]) -> HttpResponseBase: ...

class AsyncClientHandler(BaseHandler):
    enforce_csrf_checks: bool = ...
    def __init__(self, enforce_csrf_checks: bool = ..., *args: Any, **kwargs: Any) -> None: ...
    async def __call__(self, scope: dict[str, Any]) -> HttpResponseBase: ...

def encode_multipart(boundary: str, data: dict[str, Any]) -> bytes: ...
def encode_file(boundary: str, key: str, file: Any) -> list[bytes]: ...

_RequestData: TypeAlias = Any | None

class RequestFactory:
    json_encoder: type[JSONEncoder]
    defaults: dict[str, str]
    cookies: SimpleCookie
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
        path: _StrOrPromise,
        data: _RequestData = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def post(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def head(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def trace(
        self,
        path: _StrOrPromise,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def options(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def put(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def patch(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def delete(
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...
    def generic(
        self,
        method: str,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str | None = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: object,
    ) -> WSGIRequest: ...

class AsyncRequestFactory(RequestFactory): ...

class ClientMixin:
    def store_exc_info(self, **kwargs: Any) -> None: ...
    def check_exception(self, response: HttpResponse) -> None: ...
    @property
    def session(self) -> SessionBase: ...
    async def asession(self) -> SessionBase: ...
    def login(self, **credentials: Any) -> bool: ...
    async def alogin(self, **credentials: Any) -> bool: ...
    def force_login(self, user: AbstractBaseUser, backend: str | None = ...) -> None: ...
    async def aforce_login(self, user: AbstractBaseUser, backend: str | None = ...) -> None: ...
    def logout(self) -> None: ...
    async def alogout(self) -> None: ...

class Client(ClientMixin, RequestFactory):
    handler: ClientHandler
    raise_request_exception: bool
    exc_info: tuple[type[BaseException], BaseException, TracebackType] | None
    headers: dict[str, Any] | None
    def __init__(
        self,
        enforce_csrf_checks: bool = ...,
        raise_request_exception: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: Mapping[str, Any] | None = ...,
        **defaults: Any,
    ) -> None: ...
    # Silence type warnings, since this class overrides arguments and return types in an unsafe manner.
    def request(self, **request: Any) -> HttpResponse: ...  # type: ignore [override]
    def get(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def post(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def head(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def options(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def put(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def patch(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def delete(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    def trace(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...

class AsyncClient(ClientMixin, AsyncRequestFactory):
    handler: AsyncClientHandler
    raise_request_exception: bool
    exc_info: tuple[type[BaseException], BaseException, TracebackType] | None
    extra: dict[str, Any] | None = ...
    headers: dict[str, Any] | None = ...
    def __init__(
        self,
        enforce_csrf_checks: bool = ...,
        raise_request_exception: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: Mapping[str, Any] | None = ...,
        **defaults: Any,
    ) -> None: ...
    # Silence type warnings, since this class overrides arguments and return types in an unsafe manner.
    async def request(self, **request: Any) -> HttpResponse: ...  # type: ignore [override]
    async def get(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def post(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def head(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def options(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def put(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def patch(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def delete(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        content_type: str = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...
    async def trace(  # type: ignore [override]
        self,
        path: _StrOrPromise,
        data: _RequestData = ...,
        follow: bool = ...,
        secure: bool = ...,
        *,
        headers: Mapping[str, Any] | None = ...,
        query_params: str | None = ...,
        **extra: str,
    ) -> HttpResponse: ...

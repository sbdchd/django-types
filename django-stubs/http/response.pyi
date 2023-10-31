import datetime
from collections.abc import AsyncIterable, Iterable, Iterator
from io import BytesIO
from json import JSONEncoder
from typing import Any, overload

from django.core.handlers.wsgi import WSGIRequest
from django.http.cookie import SimpleCookie
from django.template import Context, Template
from django.test.client import Client
from django.urls import ResolverMatch
from django.utils.datastructures import CaseInsensitiveMapping
from typing_extensions import Never

class ResponseHeaders(CaseInsensitiveMapping[str]):
    def pop(self, key: str, default: str | None = ...) -> str: ...
    def setdefault(self, key: str, value: str) -> None: ...

class BadHeaderError(ValueError): ...

class HttpResponseBase:
    cookies: SimpleCookie
    headers: ResponseHeaders
    status_code: int
    closed: bool
    def __init__(
        self,
        content_type: str | None = ...,
        status: int | None = ...,
        reason: str | None = ...,
        charset: str | None = ...,
    ) -> None: ...
    @property
    def reason_phrase(self) -> str: ...
    @property
    def charset(self) -> str: ...
    def serialize_headers(self) -> bytes: ...
    def __setitem__(self, header: str | bytes, value: str | bytes | int) -> None: ...
    def __delitem__(self, header: str | bytes) -> None: ...
    def __getitem__(self, header: str | bytes) -> str: ...
    def has_header(self, header: str) -> bool: ...
    def items(self) -> Iterable[tuple[str, str]]: ...
    @overload
    def get(self, header: str | bytes, alternate: str | None) -> str: ...
    @overload
    def get(self, header: str | bytes) -> str | None: ...
    def set_cookie(
        self,
        key: str,
        value: str = ...,
        max_age: int | None = ...,
        expires: str | datetime.datetime | None = ...,
        path: str = ...,
        domain: str | None = ...,
        secure: bool = ...,
        httponly: bool = ...,
        samesite: str = ...,
    ) -> None: ...
    def setdefault(self, key: str, value: str) -> None: ...
    def set_signed_cookie(
        self, key: str, value: str, salt: str = ..., **kwargs: Any
    ) -> None: ...
    def delete_cookie(
        self, key: str, path: str = ..., domain: str | None = ...
    ) -> None: ...
    def make_bytes(self, value: object) -> bytes: ...
    def close(self) -> None: ...
    def write(self, content: str | bytes) -> Never: ...
    def flush(self) -> None: ...
    def tell(self) -> Never: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
    def writelines(self, lines: Iterable[str | bytes]) -> Never: ...
    def __iter__(self) -> Iterator[Any]: ...

class HttpResponse(HttpResponseBase, Iterable[bytes]):
    content: bytes
    csrf_cookie_set: bool
    redirect_chain: list[tuple[str, int]]
    sameorigin: bool
    test_server_port: str
    test_was_secure_request: bool
    xframe_options_exempt: bool
    streaming: bool
    def __init__(self, content: bytes = ..., *args: Any, **kwargs: Any) -> None: ...
    def serialize(self) -> bytes: ...
    @property
    # Attributes assigned by monkey-patching in test client ClientHandler.__call__()
    wsgi_request: WSGIRequest
    # Attributes assigned by monkey-patching in test client Client.request()
    client: Client
    request: dict[str, Any]
    templates: list[Template]
    context: Context
    resolver_match: ResolverMatch
    def json(self) -> Any: ...
    def getvalue(self) -> bytes: ...

class StreamingHttpResponse(HttpResponseBase):
    streaming_content: Iterable[bytes] | AsyncIterable[bytes]
    def __init__(
        self,
        streaming_content: Iterable[bytes] | AsyncIterable[bytes] = ...,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
    def getvalue(self) -> bytes: ...
    @property
    def content(self) -> Never: ...

class FileResponse(StreamingHttpResponse):
    client: Client
    context: None
    file_to_stream: BytesIO | None
    request: dict[str, str]
    resolver_match: ResolverMatch
    templates: list[Any]
    wsgi_request: WSGIRequest
    block_size: int = ...
    as_attachment: bool = ...
    filename: str = ...
    def __init__(
        self, *args: Any, as_attachment: bool = ..., filename: str = ..., **kwargs: Any
    ) -> None: ...
    def set_headers(self, filelike: BytesIO) -> None: ...
    def json(self) -> dict[str, Any]: ...

class HttpResponseRedirectBase(HttpResponse):
    allowed_schemes: list[str] = ...
    def __init__(self, redirect_to: str, *args: Any, **kwargs: Any) -> None: ...
    @property
    def url(self) -> str: ...

class HttpResponseRedirect(HttpResponseRedirectBase): ...
class HttpResponsePermanentRedirect(HttpResponseRedirectBase): ...

class HttpResponseNotModified(HttpResponse):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HttpResponseBadRequest(HttpResponse): ...
class HttpResponseNotFound(HttpResponse): ...
class HttpResponseForbidden(HttpResponse): ...

class HttpResponseNotAllowed(HttpResponse):
    def __init__(
        self, permitted_methods: Iterable[str], *args: Any, **kwargs: Any
    ) -> None: ...

class HttpResponseGone(HttpResponse): ...
class HttpResponseServerError(HttpResponse): ...
class Http404(Exception): ...

class JsonResponse(HttpResponse):
    def __init__(
        self,
        data: Any,
        encoder: type[JSONEncoder] = ...,
        safe: bool = ...,
        json_dumps_params: dict[str, Any] | None = ...,
        **kwargs: Any
    ) -> None: ...

from collections.abc import Callable
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class XViewMiddleware(MiddlewareMixin):
    def process_view(
        self,
        request: WSGIRequest,
        view_func: Callable[..., Any],
        view_args: tuple[Any, ...],
        view_kwargs: dict[Any, Any],
    ) -> HttpResponse | None: ...

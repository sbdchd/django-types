from collections import OrderedDict
from collections.abc import Callable
from typing import Any

from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

def x_robots_tag(func: Callable[..., Any]) -> Callable[..., Any]: ...
def index(
    request: HttpRequest,
    sitemaps: dict[str, type[Sitemap] | Sitemap],
    template_name: str = ...,
    content_type: str = ...,
    sitemap_url_name: str = ...,
) -> TemplateResponse: ...
def sitemap(
    request: HttpRequest,
    sitemaps: (
        dict[str, type[Sitemap]] | dict[str, GenericSitemap] | OrderedDict[Any, Any]
    ),
    section: str | None = ...,
    template_name: str = ...,
    content_type: str = ...,
) -> TemplateResponse: ...

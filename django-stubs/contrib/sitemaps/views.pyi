from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, TypeVar

from django.contrib.sitemaps import Sitemap
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

_C = TypeVar("_C", bound=Callable[..., Any])
_T = TypeVar("_T")

@dataclass
class SitemapIndexItem:
    location: str
    last_mod: bool | None = ...

def x_robots_tag(func: _C) -> _C: ...
def index(
    request: HttpRequest,
    sitemaps: Mapping[str, type[Sitemap[_T]] | Sitemap[_T]],
    template_name: str = ...,
    content_type: str = ...,
    sitemap_url_name: str = ...,
) -> TemplateResponse: ...
def sitemap(
    request: HttpRequest,
    sitemaps: Mapping[str, type[Sitemap[_T]] | Sitemap[_T]],
    section: str | None = ...,
    template_name: str = ...,
    content_type: str = ...,
) -> TemplateResponse: ...

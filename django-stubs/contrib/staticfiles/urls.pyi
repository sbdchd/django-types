from typing import Any

from django.urls.resolvers import URLPattern

urlpatterns: list[Any] = ...

def staticfiles_urlpatterns(prefix: str | None = ...) -> list[URLPattern]: ...

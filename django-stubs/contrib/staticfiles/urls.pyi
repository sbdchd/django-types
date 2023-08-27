from typing import Any, Optional

from django.urls.resolvers import URLPattern

urlpatterns: list[Any] = ...

def staticfiles_urlpatterns(prefix: Optional[str] = ...) -> list[URLPattern]: ...

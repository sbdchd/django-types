from typing import Any, ClassVar, TypeVar
from typing_extensions import Self

from django.db import models
from django.http.request import HttpRequest

SITE_CACHE: dict[Any, Site]

_SiteT = TypeVar("_SiteT", bound=Site)

class SiteManager(models.Manager[_SiteT]):
    def get_current(self, request: HttpRequest | None = ...) -> _SiteT: ...
    def clear_cache(self) -> None: ...
    def get_by_natural_key(self, domain: str) -> _SiteT: ...

class Site(models.Model):
    objects: ClassVar[SiteManager[Self]]  # type: ignore[assignment]

    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    def natural_key(self) -> tuple[str]: ...

def clear_site_cache(sender: type[Site], **kwargs: Any) -> None: ...

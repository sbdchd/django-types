from collections.abc import Callable, Iterable, MutableMapping
from typing import Any, Generic, TypeVar
from typing_extensions import Self

from django.db.models.base import Model
from django.db.models.query import QuerySet

_T = TypeVar("_T", bound=Model)
_V = TypeVar("_V", bound=Model)

class BaseManager(QuerySet[_T]):
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    name: str = ...
    model: type[_T] = ...
    db: str
    _db: str | None
    def __init__(self) -> None: ...
    def deconstruct(
        self,
    ) -> tuple[
        bool, str | None, str | None, tuple[Any, ...] | None, dict[str, Any] | None
    ]: ...
    def check(self, **kwargs: Any) -> list[Any]: ...
    @classmethod
    def from_queryset(
        cls, queryset_class: type[QuerySet[_T]], class_name: str | None = ...
    ) -> type[Self]: ...
    @classmethod
    def _get_queryset_methods(
        cls, queryset_class: type[QuerySet[_T]]
    ) -> dict[str, Callable[..., Any]]: ...
    def contribute_to_class(self, model: type[Model], name: str) -> None: ...
    def db_manager(
        self, using: str | None = ..., hints: dict[str, Model] | None = ...
    ) -> Self: ...
    def get_queryset(self) -> QuerySet[_T]: ...

class Manager(BaseManager[_T]):
    _queryset_class: type[QuerySet[_T]]

class RelatedManager(Manager[_T]):
    related_val: tuple[int, ...]
    def __call__(self, *, manager: str) -> RelatedManager[_T]: ...
    def add(self, *objs: QuerySet[_T] | _T, bulk: bool = ...) -> None: ...
    async def aadd(self, *objs: QuerySet[_T] | _T, bulk: bool = ...) -> None: ...
    def remove(self, *objs: QuerySet[_T] | _T, bulk: bool = ...) -> None: ...
    async def aremove(self, *objs: QuerySet[_T] | _T, bulk: bool = ...) -> None: ...
    def set(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        bulk: bool = ...,
        clear: bool = ...,
    ) -> None: ...
    async def aset(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        bulk: bool = ...,
        clear: bool = ...,
    ) -> None: ...
    def clear(self) -> None: ...
    async def aclear(self) -> None: ...

class ManyToManyRelatedManager(Generic[_T, _V], Manager[_T]):
    through: type[_V]
    def __call__(self, *, manager: str) -> ManyToManyRelatedManager[_T, _V]: ...
    def add(
        self,
        *objs: QuerySet[_T] | _T | _V,
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    async def aadd(
        self,
        *objs: QuerySet[_T] | _T | _V,
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    def remove(self, *objs: QuerySet[_T] | _T | _V) -> None: ...
    async def aremove(self, *objs: QuerySet[_T] | _T | _V) -> None: ...
    def set(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        clear: bool = ...,
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    async def aset(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        clear: bool = ...,
        through_defaults: MutableMapping[str, Any] = ...,
    ) -> None: ...
    def clear(self) -> None: ...
    async def aclear(self) -> None: ...
    def create(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        through_defaults: MutableMapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> _T: ...
    async def acreate(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        through_defaults: MutableMapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> _T: ...
    def get_or_create(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    async def aget_or_create(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    def update_or_create(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    async def aupdate_or_create(
        self,
        defaults: MutableMapping[str, Any] | None = ...,
        *,
        through_defaults: MutableMapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...

class ManagerDescriptor:
    manager: Manager[Any] = ...
    def __init__(self, manager: Manager[Any]) -> None: ...
    def __get__(
        self, instance: Model | None, cls: type[Model] = ...
    ) -> Manager[Any]: ...

class EmptyManager(Manager[_T]):
    def __init__(self, model: type[_T]) -> None: ...

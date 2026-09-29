from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Generic, overload

from django.db.models.base import Model
from django.db.models.expressions import Combinable, OrderBy
from django.db.models.query import QuerySet
from typing_extensions import Self, TypeVar

_T = TypeVar("_T", bound=Model)
_V = TypeVar("_V", bound=Model)
# Manager proxies chain calls to get_queryset(), so they return the queryset, not the manager.
_QS = TypeVar("_QS", bound=QuerySet[Any, Any], default=QuerySet[_T])

class BaseManager(QuerySet[_T], Generic[_T, _QS]):
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
    ) -> tuple[bool, str | None, str | None, tuple[Any, ...] | None, dict[str, Any] | None]: ...
    def check(self, **kwargs: Any) -> list[Any]: ...
    @classmethod
    def from_queryset(cls, queryset_class: type[QuerySet[_T]], class_name: str | None = ...) -> type[Self]: ...
    @classmethod
    def _get_queryset_methods(cls, queryset_class: type[QuerySet[_T]]) -> dict[str, Callable[..., Any]]: ...
    def contribute_to_class(self, model: type[Model], name: str) -> None: ...
    def db_manager(self, using: str | None = ..., hints: dict[str, Model] | None = ...) -> Self: ...
    def get_queryset(self) -> _QS: ...
    # Managers aren't QuerySets at runtime; these proxies return get_queryset(), not Self.
    def none(self) -> _QS: ...  # type: ignore[override]
    def all(self) -> _QS: ...  # type: ignore[override]
    def filter(self, *args: Any, **kwargs: Any) -> _QS: ...  # type: ignore[override]
    def exclude(self, *args: Any, **kwargs: Any) -> _QS: ...  # type: ignore[override]
    def complex_filter(self, filter_obj: Any) -> _QS: ...  # type: ignore[override]
    def union(self, *other_qs: QuerySet[Model, Any], all: bool = False) -> _QS: ...  # type: ignore[override]
    def intersection(self, *other_qs: QuerySet[Model, Any]) -> _QS: ...  # type: ignore[override]
    def difference(self, *other_qs: QuerySet[Model, Any]) -> _QS: ...  # type: ignore[override]
    def select_for_update(  # type: ignore[override]
        self, nowait: bool = False, skip_locked: bool = False, of: Sequence[str] = (), no_key: bool = False
    ) -> _QS: ...
    @overload  # type: ignore[override]
    def select_related(self, clear: None, /) -> _QS: ...
    @overload
    def select_related(self, *fields: str) -> _QS: ...
    def prefetch_related(self, *lookups: Any) -> _QS: ...  # type: ignore[override]
    def annotate(self, *args: Any, **kwargs: Any) -> _QS: ...  # type: ignore[override]
    def alias(self, *args: Any, **kwargs: Any) -> _QS: ...  # type: ignore[override]
    def order_by(self, *field_names: str | Combinable | OrderBy) -> _QS: ...  # type: ignore[override]
    def distinct(self, *field_names: str) -> _QS: ...  # type: ignore[override]
    def reverse(self) -> _QS: ...  # type: ignore[override]
    @overload  # type: ignore[override]
    def defer(self, clear: None, /) -> _QS: ...
    @overload
    def defer(self, *fields: str) -> _QS: ...
    def only(self, *fields: str) -> _QS: ...  # type: ignore[override]
    def using(self, alias: str | None) -> _QS: ...  # type: ignore[override]

class Manager(BaseManager[_T, _QS]):
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

class ManyToManyRelatedManager(Manager[_T], Generic[_T, _V]):
    through: type[_V]
    def __call__(self, *, manager: str) -> ManyToManyRelatedManager[_T, _V]: ...
    def add(
        self,
        *objs: QuerySet[_T] | _T | _V,
        through_defaults: Mapping[str, Any] = ...,
    ) -> None: ...
    async def aadd(
        self,
        *objs: QuerySet[_T] | _T | _V,
        through_defaults: Mapping[str, Any] = ...,
    ) -> None: ...
    def remove(self, *objs: QuerySet[_T] | _T | _V) -> None: ...
    async def aremove(self, *objs: QuerySet[_T] | _T | _V) -> None: ...
    def set(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        clear: bool = ...,
        through_defaults: Mapping[str, Any] = ...,
    ) -> None: ...
    async def aset(
        self,
        objs: QuerySet[_T] | Iterable[_T],
        *,
        clear: bool = ...,
        through_defaults: Mapping[str, Any] = ...,
    ) -> None: ...
    def clear(self) -> None: ...
    async def aclear(self) -> None: ...
    def create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        through_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> _T: ...
    async def acreate(
        self,
        defaults: Mapping[str, Any] | None = ...,
        through_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> _T: ...
    def get_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        *,
        through_defaults: Mapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    async def aget_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        *,
        through_defaults: Mapping[str, Any] = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    def update_or_create(
        self,
        defaults: Mapping[str, Any] | None = None,
        create_defaults: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    async def aupdate_or_create(
        self,
        defaults: Mapping[str, Any] | None = None,
        create_defaults: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...

class ManagerDescriptor:
    manager: Manager[Any] = ...
    def __init__(self, manager: Manager[Any]) -> None: ...
    def __get__(self, instance: Model | None, cls: type[Model] = ...) -> Manager[Any]: ...

class EmptyManager(Manager[_T]):
    def __init__(self, model: type[_T]) -> None: ...

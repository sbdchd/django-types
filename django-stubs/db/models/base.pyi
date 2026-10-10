from collections.abc import Callable, Collection, Iterable
from typing import Any, ClassVar, TypeVar, overload

from django.core.checks.messages import CheckMessage
from django.core.exceptions import MultipleObjectsReturned as BaseMultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models.manager import Manager
from django.db.models.options import Options
from django.db.models.query import QuerySet
from typing_extensions import Self

class Deferred: ...

DEFERRED: Deferred

class ModelStateFieldsCacheDescriptor: ...

class ModelState:
    db: str | None = ...
    adding: bool = ...
    fields_cache: ModelStateFieldsCacheDescriptor = ...

_M = TypeVar("_M", bound=Model)

class _DefaultManager:
    # Declared on the metaclass and without __set__, so a model's own `objects`
    # (any manager type) shadows it with no override conflict; instance access
    # stays an error, as Django's ManagerDescriptor raises there.
    @overload
    def __get__(self, instance: type[_M], owner: type[ModelBase]) -> Manager[_M]: ...
    # mypy binds a metaclass descriptor as (None, cls).
    @overload
    def __get__(self, instance: None, owner: type[_M]) -> Manager[_M]: ...

class ModelBase(type):
    objects: ClassVar[_DefaultManager]

class Model(metaclass=ModelBase):
    DoesNotExist: ClassVar[type[ObjectDoesNotExist]]
    MultipleObjectsReturned: ClassVar[type[BaseMultipleObjectsReturned]]
    _meta: ClassVar[Options[Self]]
    _default_manager: ClassVar[Manager[Self]]

    pk: Any = ...
    _state: ModelState
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def add_to_class(cls, name: str, value: Any) -> Any: ...
    @classmethod
    def from_db(cls, db: str | None, field_names: Collection[str], values: Collection[Any]) -> Self: ...
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]: ...
    async def adelete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]: ...
    def full_clean(
        self,
        exclude: Collection[str] | None = ...,
        validate_unique: bool = ...,
        validate_constraints: bool = ...,
    ) -> None: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: Collection[str] | None = ...) -> None: ...
    def validate_unique(self, exclude: Collection[str] | None = ...) -> None: ...
    def validate_constraints(self, exclude: Collection[str] | None = ...) -> None: ...
    def unique_error_message(
        self,
        model_class: type[Self],
        unique_check: Collection[Callable[..., Any] | str],
    ) -> ValidationError: ...
    def save(
        self,
        *,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    async def asave(
        self,
        *,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> Any: ...
    def refresh_from_db(
        self,
        using: str | None = ...,
        fields: Iterable[str] | None = ...,
        from_queryset: QuerySet[Self] | None = ...,
    ) -> None: ...
    async def arefresh_from_db(
        self,
        using: str | None = ...,
        fields: Iterable[str] | None = ...,
        from_queryset: QuerySet[Self] | None = ...,
    ) -> None: ...
    def get_deferred_fields(self) -> set[str]: ...
    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    def __getstate__(self) -> dict[Any, Any]: ...

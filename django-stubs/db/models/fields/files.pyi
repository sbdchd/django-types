from collections.abc import Callable, Iterable
from typing import Any, overload
from typing_extensions import Self

from django.core.files.base import File
from django.core.files.images import ImageFile
from django.core.files.storage import FileSystemStorage, Storage
from django.db.models.base import Model
from django.db.models.fields import (
    _GT,
    Field,
    _ErrorMessagesToOverride,
    _ValidatorCallable,
)

class FieldFile(File):
    instance: Model = ...
    field: FileField = ...
    storage: FileSystemStorage = ...
    def __init__(self, instance: Model, field: FileField, name: str | None) -> None: ...
    file: Any = ...
    @property
    def path(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def size(self) -> int: ...
    def save(self, name: str, content: File, save: bool = ...) -> None: ...
    def delete(self, save: bool = ...) -> None: ...
    @property
    def closed(self) -> bool: ...

class FileDescriptor:
    field: FileField = ...
    def __init__(self, field: FileField) -> None: ...
    def __set__(self, instance: Model, value: Any | None) -> None: ...
    def __get__(
        self, instance: Model | None, cls: type[Model] = ...
    ) -> FieldFile | FileDescriptor: ...

class FileField(Field[FileDescriptor, FileDescriptor]):
    storage: Any = ...
    upload_to: str | Callable[[Any, str], str] = ...
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        upload_to: str | Callable[[Any, str], str] = ...,
        storage: Storage | Callable[[], Storage] | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: _GT | Callable[[], _GT] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_GT, str] | tuple[str, Iterable[tuple[_GT, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...
    # class access
    @overload  # type: ignore
    def __get__(self, instance: None, owner: Any) -> FileDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> FieldFile: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...
    def generate_filename(self, instance: Model | None, filename: str) -> str: ...

class ImageFileDescriptor(FileDescriptor):
    field: ImageField  # pyright: ignore[reportIncompatibleVariableOverride]
    def __set__(self, instance: Model, value: str | None) -> None: ...

class ImageFieldFile(ImageFile, FieldFile):
    field: ImageField  # pyright: ignore[reportIncompatibleVariableOverride]
    def delete(self, save: bool = ...) -> None: ...

class ImageField(FileField):
    def __new__(
        cls,
        verbose_name: str | None = ...,
        name: str | None = ...,
        width_field: str = ...,
        height_field: str = ...,
        upload_to: str | Callable[[Model, str], Any] = ...,
        storage: Storage | Callable[[], Storage] | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        default: _GT | Callable[[], _GT] | None = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[
            tuple[_GT, str] | tuple[str, Iterable[tuple[_GT, str]]]
        ] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
    ) -> Self: ...
    # class access
    @overload  # type: ignore
    def __get__(self, instance: None, owner: Any) -> ImageFileDescriptor: ...
    # Model instance access
    @overload
    def __get__(self, instance: Model, owner: Any) -> ImageFieldFile: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...
    def update_dimension_fields(
        self, instance: Model, force: bool = ..., *args: Any, **kwargs: Any
    ) -> None: ...

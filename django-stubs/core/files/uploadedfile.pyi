from typing import IO, Any

from django.core.files.base import File

class UploadedFile(File):
    content_type: str | None = ...
    charset: str | None = ...
    content_type_extra: dict[str, str] | None = ...
    def __init__(
        self,
        file: IO[Any] | None = ...,
        name: str | None = ...,
        content_type: str | None = ...,
        size: int | None = ...,
        charset: str | None = ...,
        content_type_extra: dict[str, str] | None = ...,
    ) -> None: ...

class TemporaryUploadedFile(UploadedFile):
    def __init__(
        self,
        name: str | None,
        content_type: str | None,
        size: int | None,
        charset: str | None,
        content_type_extra: dict[str, str] | None = ...,
    ) -> None: ...
    def temporary_file_path(self) -> str: ...

class InMemoryUploadedFile(UploadedFile):
    field_name: str | None = ...
    def __init__(
        self,
        file: IO[Any],
        field_name: str | None,
        name: str | None,
        content_type: str | None,
        size: int | None,
        charset: str | None,
        content_type_extra: dict[str, str] = ...,
    ) -> None: ...

class SimpleUploadedFile(InMemoryUploadedFile):
    def __init__(
        self, name: str, content: bytes | str | None, content_type: str = ...
    ) -> None: ...
    @classmethod
    def from_dict(cls, file_dict: dict[str, str | bytes]) -> None: ...

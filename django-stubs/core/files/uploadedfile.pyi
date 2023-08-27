from typing import IO, Any, Optional, Union

from django.core.files.base import File

class UploadedFile(File):
    content_type: Optional[str] = ...
    charset: Optional[str] = ...
    content_type_extra: Optional[dict[str, str]] = ...
    def __init__(
        self,
        file: Optional[IO[Any]] = ...,
        name: Optional[str] = ...,
        content_type: Optional[str] = ...,
        size: Optional[int] = ...,
        charset: Optional[str] = ...,
        content_type_extra: Optional[dict[str, str]] = ...,
    ) -> None: ...

class TemporaryUploadedFile(UploadedFile):
    def __init__(
        self,
        name: Optional[str],
        content_type: Optional[str],
        size: Optional[int],
        charset: Optional[str],
        content_type_extra: Optional[dict[str, str]] = ...,
    ) -> None: ...
    def temporary_file_path(self) -> str: ...

class InMemoryUploadedFile(UploadedFile):
    field_name: Optional[str] = ...
    def __init__(
        self,
        file: IO[Any],
        field_name: Optional[str],
        name: Optional[str],
        content_type: Optional[str],
        size: Optional[int],
        charset: Optional[str],
        content_type_extra: dict[str, str] = ...,
    ) -> None: ...

class SimpleUploadedFile(InMemoryUploadedFile):
    def __init__(
        self, name: str, content: Optional[Union[bytes, str]], content_type: str = ...
    ) -> None: ...
    @classmethod
    def from_dict(cls, file_dict: dict[str, Union[str, bytes]]) -> None: ...

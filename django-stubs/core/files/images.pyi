from typing import IO, Any

from django.core.files import File

class ImageFile(File):
    mode: str
    name: str
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...

def get_image_dimensions(file_or_path: str | IO[bytes], close: bool = ...) -> Any: ...

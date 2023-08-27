from typing import Any, Union

from django.contrib.messages.storage.base import BaseStorage
from django.http.request import HttpRequest

def messages(
    request: HttpRequest,
) -> dict[str, Union[dict[str, int], list[Any], BaseStorage]]: ...

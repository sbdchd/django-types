import json
from typing import Any

from django.core.serializers.python import Serializer as PythonSerializer

class Serializer(PythonSerializer):
    json_kwargs: dict[str, Any]

def Deserializer(stream_or_string: Any, **options: Any) -> None: ...

class DjangoJSONEncoder(json.JSONEncoder):
    allow_nan: bool
    check_circular: bool
    ensure_ascii: bool
    indent: int  # pyright: ignore[reportIncompatibleVariableOverride]
    skipkeys: bool
    sort_keys: bool

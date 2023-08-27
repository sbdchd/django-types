from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig
from django.contrib.admin.options import BaseModelAdmin
from django.core.checks.messages import CheckMessage, Error

_CheckError = str | Error

def check_admin_app(
    app_configs: Sequence[AppConfig] | None = ..., **kwargs: Any
) -> list[_CheckError]: ...
def check_dependencies(**kwargs: Any) -> list[_CheckError]: ...

class BaseModelAdminChecks:
    def check(
        self, admin_obj: BaseModelAdmin[Any], **kwargs: Any
    ) -> list[CheckMessage]: ...

class ModelAdminChecks(BaseModelAdminChecks): ...
class InlineModelAdminChecks(BaseModelAdminChecks): ...

def must_be(type: Any, option: Any, obj: Any, id: Any) -> Any: ...
def must_inherit_from(parent: Any, option: Any, obj: Any, id: Any) -> Any: ...
def refer_to_missing_field(
    field: Any, option: Any, model: Any, obj: Any, id: Any
) -> Any: ...

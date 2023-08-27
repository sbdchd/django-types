from typing import Any

from django.db import models

class CurrentSiteManager(models.Manager[Any]):
    def __init__(self, field_name: str | None = ...) -> None: ...

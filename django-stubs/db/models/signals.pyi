from collections.abc import Callable
from typing import Any, Optional, Union

from django.apps.registry import Apps
from django.db.models.base import Model
from django.dispatch import Signal

class_prepared: Signal

class ModelSignal(Signal):
    def connect(  # type: ignore
        self,
        receiver: Callable[..., Any],
        sender: Optional[Union[type[Model], str]] = ...,
        weak: bool = ...,
        dispatch_uid: Optional[str] = ...,
        apps: Optional[Apps] = ...,
    ) -> None: ...
    def disconnect(  # type: ignore
        self,
        receiver: Callable[..., Any] = ...,
        sender: Optional[Union[type[Model], str]] = ...,
        dispatch_uid: Optional[str] = ...,
        apps: Optional[Apps] = ...,
    ) -> Optional[bool]: ...

pre_init: ModelSignal
post_init: ModelSignal
pre_save: ModelSignal
post_save: ModelSignal
pre_delete: ModelSignal
post_delete: ModelSignal
m2m_changed: ModelSignal
pre_migrate: Signal
post_migrate: Signal

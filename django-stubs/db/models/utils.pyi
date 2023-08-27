from typing import Union

from django.db.models.base import Model

def make_model_tuple(model: Union[type[Model], str]) -> tuple[str, str]: ...

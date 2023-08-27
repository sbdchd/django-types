from collections.abc import Iterable
from typing import Any, Optional

TEMPLATE_FRAGMENT_KEY_TEMPLATE: str

def make_template_fragment_key(
    fragment_name: str, vary_on: Optional[Iterable[Any]] = ...
) -> str: ...

from collections.abc import Sequence

from django.db.models.constraints import BaseConstraint
from django.db.models.expressions import Combinable
from django.db.models.query_utils import Q

class ExclusionConstraint(BaseConstraint):
    expressions: Sequence[tuple[str | Combinable, str]]
    index_type: str
    condition: Q | None
    def __init__(
        self,
        *,
        name: str,
        expressions: Sequence[tuple[str | Combinable, str]],
        condition: Q | None = ...,
        index_type: str | None = ...,
    ) -> None: ...

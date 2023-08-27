from collections.abc import Iterator

from django.db.migrations.operations.base import Operation

def topological_sort_as_sets(
    dependency_graph: dict[Operation, set[Operation]]
) -> Iterator[set[Operation]]: ...
def stable_topological_sort(
    l: list[Operation], dependency_graph: dict[Operation, set[Operation]]  # noqa:E741
) -> list[Operation]: ...

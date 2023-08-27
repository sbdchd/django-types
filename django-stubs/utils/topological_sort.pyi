from collections.abc import Container, Iterator
from typing import Any

class CyclicDependencyError(ValueError): ...

def topological_sort_as_sets(
    dependency_graph: dict[Any, Any]
) -> Iterator[set[Any]]: ...
def stable_topological_sort(
    l: Container[Any], dependency_graph: dict[Any, Any]  # noqa:E741
) -> list[Any]: ...

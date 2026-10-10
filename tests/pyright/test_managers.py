from .base import run_pyright


def test_managers_reject_queryset_only_operations() -> None:
    results = run_pyright("""\
from django.db.models import Manager, Model, QuerySet

def wrong(manager: Manager[Model], qs: QuerySet[Model]) -> None:
    for _item in manager:
        pass
    _ = len(manager)
    _ = manager[0]
    manager.delete()
    _ = manager.query
    _ = manager & qs
""")
    error_lines = {r.line for r in results if r.type == "error"}
    assert {4, 6, 7, 8, 9, 10} <= error_lines, results

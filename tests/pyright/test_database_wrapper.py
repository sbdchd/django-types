from .base import Result, run_pyright


def test_base_database_wrapper_declares_its_public_members() -> None:
    """Every public attribute and method BaseDatabaseWrapper defines is visible to the checker."""
    results = run_pyright(
        """\
from django.db import connection

connection.inc_thread_sharing()
connection.dec_thread_sharing()
connection.check_database_version_supported()
connection.close_if_health_check_failed()
connection.get_database_version()
reveal_type(connection.atomic_blocks)
reveal_type(connection.health_check_done)
reveal_type(connection.health_check_enabled)
reveal_type(connection.rollback_exc)
"""
    )
    assert results == [
        Result(type="information", message='Type of "connection.atomic_blocks" is "list[Atomic]"', line=8, column=13),
        Result(type="information", message='Type of "connection.health_check_done" is "bool"', line=9, column=13),
        Result(type="information", message='Type of "connection.health_check_enabled" is "bool"', line=10, column=13),
        Result(type="information", message='Type of "connection.rollback_exc" is "Exception | None"', line=11, column=13),
    ]


def test_context_manager_methods_are_usable_in_with() -> None:
    """execute_wrapper and constraint_checks_disabled are @contextmanager at runtime."""
    results = run_pyright(
        """\
from django.db import connection

def wrapper(*args: object) -> None: ...

with connection.execute_wrapper(wrapper) as entered:
    reveal_type(entered)
with connection.constraint_checks_disabled():
    pass
"""
    )
    assert results == [
        Result(type="information", message='Type of "entered" is "None"', line=6, column=17),
    ]

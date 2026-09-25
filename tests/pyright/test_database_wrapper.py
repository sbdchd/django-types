from .base import Result, run_pyright


def test_atomic_blocks_and_thread_sharing_are_declared() -> None:
    """A test helper hands a connection to another thread and inspects the open atomic blocks."""
    results = run_pyright(
        """\
from django.db import connection

connection.inc_thread_sharing()
connection.dec_thread_sharing()
reveal_type(connection.atomic_blocks)
"""
    )
    assert [r for r in results if r.type == "error"] == []
    assert results == [
        Result(type="information", message='Type of "connection.atomic_blocks" is "list[Atomic]"', line=5, column=13),
    ]

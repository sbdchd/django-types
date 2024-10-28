from .base import Result, run_pyright


def test_array_field() -> None:
    results = run_pyright(
        """\
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Foo(models.Model):
    array = ArrayField(
        models.CharField(max_length=10, blank=True),
    )

f = Foo()
reveal_type(f.array)
reveal_type(f.array[0])
f.array = ["a", "b"]
f.array = [1, 2]
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.array" is "list[str]"',
            line=10,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0]" is "str"',
            line=11,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "array" for class "Foo"',
            line=13,
            column=3,
        ),
    ]


def test_array_field_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Foo(models.Model):
    array = ArrayField(
        models.CharField(max_length=10, blank=True),
        null=True,
    )

f = Foo()
reveal_type(f.array)
reveal_type(f.array[0])
f.array = ["a", "b"]
f.array = None
f.array = [1, 2]
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.array" is "list[str] | None"',
            line=11,
            column=13,
        ),
        Result(
            type="error",
            message='Object of type "None" is not subscriptable (reportOptionalSubscript)',
            line=12,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0]" is "str | Unknown"',
            line=12,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "array" for class "Foo"',
            line=15,
            column=3,
        ),
    ]


def test_array_multiple_field() -> None:
    results = run_pyright(
        """\
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Foo(models.Model):
    array = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )

f = Foo()
reveal_type(f.array)
reveal_type(f.array[0])
reveal_type(f.array[0][0])
f.array = [["a", "b"], ["c"]]
f.array = ["a", "b"]
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.array" is "list[list[str]]"',
            line=14,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0]" is "list[str]"',
            line=15,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0][0]" is "str"',
            line=16,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "array" for class "Foo"',
            line=18,
            column=3,
        ),
    ]


def test_array_multiple_field_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Foo(models.Model):
    array = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
        null=True,
    )

f = Foo()
reveal_type(f.array)
reveal_type(f.array[0])
reveal_type(f.array[0][0])
f.array = [["a", "b"], ["c"]]
f.array = ["a", "b"]
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.array" is "list[list[str]] | None"',
            line=15,
            column=13,
        ),
        Result(
            type="error",
            message='Object of type "None" is not subscriptable (reportOptionalSubscript)',
            line=16,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0]" is "list[str] | Unknown"',
            line=16,
            column=13,
        ),
        Result(
            type="error",
            message='Object of type "None" is not subscriptable (reportOptionalSubscript)',
            line=17,
            column=13,
        ),
        Result(
            type="information",
            message='Type of "f.array[0][0]" is "str | Unknown"',
            line=17,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "array" for class "Foo"',
            line=19,
            column=3,
        ),
    ]

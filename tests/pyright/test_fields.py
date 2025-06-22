from .base import Result, run_pyright


def test_integer_with_choices() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    integer_with_choices = models.IntegerField(
        choices=[
            (1, "First Option"),
            (2, "Second Option"),
        ],
    )

f = Foo()
reveal_type(f.integer_with_choices)
res = f.integer_with_choices == 2
res = f.integer_with_choices == 3
f.integer_with_choices = None
f.integer_with_choices = 3
f.integer_with_choices = 2
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.integer_with_choices" is "int"',
            line=12,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "integer_with_choices" for class "Foo"',
            line=15,
            column=3,
        ),
    ]


def test_integer_with_choices_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    integer_with_choices_nullable = models.IntegerField(
        choices=[
            (1, "First Option"),
            (2, "Second Option"),
        ],
        null=True,
    )

f = Foo()
reveal_type(f.integer_with_choices_nullable)
res = f.integer_with_choices_nullable == 2
res = f.integer_with_choices_nullable == 3
f.integer_with_choices_nullable = None
f.integer_with_choices_nullable = 3
f.integer_with_choices_nullable = 2
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.integer_with_choices_nullable" is "int | None"',
            line=13,
            column=13,
        ),
    ]


def test_char_with_choices() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    char_with_choices = models.CharField(
        choices=[
            ("a", "A"),
            ("b", "B"),
        ],
    )

f = Foo()
reveal_type(f.char_with_choices)
res = f.char_with_choices == "c"
res = f.char_with_choices == "a"
f.char_with_choices = None
f.char_with_choices = "c"
f.char_with_choices = "b"
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.char_with_choices" is "str"',
            line=12,
            column=13,
        ),
        Result(
            type="error",
            message='Cannot assign to attribute "char_with_choices" for class "Foo"',
            line=15,
            column=3,
        ),
    ]


def test_char_with_choices_nullable() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    char_with_choices_nullable = models.CharField(
        choices=[
            ("a", "A"),
            ("b", "B"),
        ],
        null=True,
    )

f = Foo()
reveal_type(f.char_with_choices_nullable)
res = f.char_with_choices_nullable == "c"
res = f.char_with_choices_nullable == "a"
f.char_with_choices_nullable = None
f.char_with_choices_nullable = "c"
f.char_with_choices_nullable = "b"
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.char_with_choices_nullable" is "str | None"',
            line=13,
            column=13,
        ),
    ]
def test_composite_primary_key_field() -> None:
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    composite = models.CompositePrimaryKey("a", "b")

f = Foo()
reveal_type(f.composite)
res = f.composite == (1, 2)
f.composite = (3, 4)
f.composite = None
"""
    )
    assert results == [
        Result(
            type="information",
            message='Type of "f.composite" is "tuple[Any, ...] | None"',
            line=9,
            column=13,
        )
    ]

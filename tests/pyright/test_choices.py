from .base import run_pyright


def test_choices_accepts_a_mapping() -> None:
    """A model declares choices as a dict, the way Django has accepted since 5.0."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    kind = models.CharField(max_length=8, choices={"a": "A", "b": "B"})
    size = models.IntegerField(choices={1: "one", 2: "two"})
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_text_field_accepts_a_text_choices_class() -> None:
    """A TextField takes a TextChoices class, exactly as a CharField does."""
    results = run_pyright(
        """\
from django.db import models

class Kind(models.TextChoices):
    A = "a", "A"

class Foo(models.Model):
    body = models.TextField(choices=Kind)
    slug = models.SlugField(choices=Kind)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_choices_accepts_a_callable() -> None:
    """A choices callable keeps a new enum member from needing a migration."""
    results = run_pyright(
        """\
from django.db import models

def flag_choices() -> list[tuple[str, str]]:
    return [("a", "A")]

class Foo(models.Model):
    flag = models.CharField(max_length=64, choices=flag_choices)
"""
    )
    assert [r for r in results if r.type == "error"] == []


def test_integer_field_still_rejects_a_text_choices_class() -> None:
    """Widening the overloads must not erase the precision they already had."""
    results = run_pyright(
        """\
from django.db import models

class Kind(models.TextChoices):
    A = "a", "A"

class Foo(models.Model):
    size = models.IntegerField(choices=Kind)
"""
    )
    errors = [r for r in results if r.type == "error"]
    assert len(errors) == 1
    assert '"choices"' in errors[0].message


def test_choices_widened_outside_fields_init() -> None:
    """The widened spellings work on JSONField, FileField, ForeignKey, ArrayField and GeneratedField."""
    results = run_pyright(
        """\
from django.contrib.postgres.fields import ArrayField
from django.db import models

class Kind(models.TextChoices):
    A = "a", "A"

def opts() -> list[tuple[str, str]]:
    return [("a", "A")]

class Thing(models.Model): ...

class Foo(models.Model):
    data = models.JSONField(choices={"a": "A"})
    doc = models.FileField(choices=Kind)
    ref = models.ForeignKey(Thing, on_delete=models.CASCADE, choices=opts)
    tags = ArrayField(models.CharField(max_length=8), choices=lambda: [(["a", "b"], "AB")])
    total = models.GeneratedField(expression=models.F("a") + models.F("b"), output_field=models.IntegerField(), db_persist=True, choices={1: "one"})
"""
    )
    assert [r for r in results if r.type == "error"] == []

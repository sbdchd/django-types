from .base import run_pyright


def test_choices_accepts_a_mapping() -> None:
    """A model declares choices as a dict, the way Django has accepted since 5.0.

    Field.choices already admitted a mapping through _ChoicesMapping, but every
    per-field __new__ overload listed only the pair iterable, so the dict form
    was rejected at the constructor.
    """
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
    """A TextField takes a TextChoices class, exactly as a CharField does.

    CharField's overloads named type[TextChoices]; TextField's did not, so the
    same enum was accepted on one string field and rejected on the other.
    """
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
    """A choices callable keeps a new enum member from needing a migration.

    Django serializes the reference rather than the values. Field.choices
    allowed the callable; the overloads did not.
    """
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
    """Widening the overloads must not erase the precision they already had.

    An IntegerField's choices are IntegerChoices; handing it a TextChoices
    class was an error before this change and stays one.
    """
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

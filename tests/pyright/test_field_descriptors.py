from .base import Result, run_pyright


def test_foreign_key_lazy_string_reference() -> None:
    """A model points at another app's model by name to avoid an import cycle."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    lazy_nullable = models.ForeignKey("other.Thing", on_delete=models.CASCADE, null=True)
    lazy_required = models.ForeignKey("other.Thing", on_delete=models.CASCADE)

f = Foo()
reveal_type(f.lazy_nullable)
reveal_type(f.lazy_required)
name: str = f.lazy_required.title
"""
    )
    assert results == [
        Result(type="information", message='Type of "f.lazy_nullable" is "Any | None"', line=8, column=13),
        Result(type="information", message='Type of "f.lazy_required" is "Any"', line=9, column=13),
    ]


def test_unparameterized_json_field() -> None:
    """A model stores a free-form JSON blob and does not parameterise the field."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    data = models.JSONField()
    maybe = models.JSONField(null=True)

f = Foo()
reveal_type(f.data)
f.data = {"a": 1}
f.data = [1, 2, 3]
f.data = "a string is valid json"
f.data = None
count: int = f.data["items"][0]["qty"]
"""
    )
    assert results == [
        Result(type="information", message='Type of "f.data" is "Any"', line=8, column=13),
    ]


def test_file_field_accepts_a_file_on_assignment() -> None:
    """Assigning an in-memory File or a path str to a FileField is accepted; reads return the descriptor."""
    results = run_pyright(
        """\
from django.core.files.base import ContentFile
from django.db import models

class Foo(models.Model):
    doc = models.FileField(upload_to="docs/")

f = Foo()
f.doc = ContentFile(b"x", name="x.txt")
f.doc = "docs/x.txt"
"""
    )
    assert results == []


def test_field_max_length_reads_as_optional() -> None:
    """Introspection code reads max_length off a field and guards for None."""
    results = run_pyright(
        """\
from django.db.models import Field

def check(field: Field) -> None:
    reveal_type(field.max_length)
"""
    )
    assert results == [
        Result(type="information", message='Type of "field.max_length" is "int | None"', line=4, column=17),
    ]


def test_foreign_key_lazy_reference_can_be_parameterised() -> None:
    """A codebase that wants precision annotates the lazy reference explicitly."""
    results = run_pyright(
        """\
from django.db import models

class Thing(models.Model):
    title = models.CharField(max_length=10)

class Foo(models.Model):
    untyped = models.ForeignKey("app.Thing", on_delete=models.CASCADE)
    typed = models.ForeignKey[Thing]("app.Thing", on_delete=models.CASCADE)
    typed_null = models.ForeignKey[Thing | None]("app.Thing", on_delete=models.CASCADE, null=True)

f = Foo()
reveal_type(f.untyped)
reveal_type(f.typed)
reveal_type(f.typed_null)
"""
    )
    assert results == [
        Result(type="information", message='Type of "f.untyped" is "Any"', line=12, column=13),
        Result(type="information", message='Type of "f.typed" is "Thing"', line=13, column=13),
        Result(type="information", message='Type of "f.typed_null" is "Thing | None"', line=14, column=13),
    ]


def test_lazy_reference_keywords_are_still_checked() -> None:
    """A typo in a keyword on a string-referenced FK is still an error; valid keywords still pass."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    ok = models.ForeignKey("app.Thing", on_delete=models.CASCADE, related_name="foos", null=True, db_index=False)
    bad = models.ForeignKey("app.Thing", on_delete=models.CASCADE, related_nme="foos")

reveal_type(Foo().ok)
"""
    )
    errors = [r for r in results if r.type == "error"]
    assert [r.line for r in errors] == [5]
    assert [r.message for r in results if r.type == "information"] == ['Type of "Foo().ok" is "Any | None"']


def test_lazy_foreign_key_keywords_and_positionals_are_checked() -> None:
    """A string reference goes through the ordinary overloads, so keywords are checked and stray positionals error."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    ok = models.ForeignKey("app.Thing", on_delete=models.CASCADE, to_field="slug", related_name="foos")
    bad = models.ForeignKey("app.Thing", models.CASCADE, ["a"], ["b"])

reveal_type(Foo().ok)
"""
    )
    assert [r.line for r in results if r.type == "error"] == [5]
    assert [r.message for r in results if r.type == "information"] == ['Type of "Foo().ok" is "Any"']


def test_lazy_one_to_one_null_reads_optional() -> None:
    """A null=True OneToOneField named by string reads Any | None, the same shape a class reference gets."""
    results = run_pyright(
        """\
from django.db import models

class Foo(models.Model):
    o2o = models.OneToOneField("app.Thing", on_delete=models.CASCADE, null=True)
    req = models.OneToOneField("app.Thing", on_delete=models.CASCADE)

reveal_type(Foo().o2o)
reveal_type(Foo().req)
"""
    )
    assert [r.message for r in results if r.type == "information"] == [
        'Type of "Foo().o2o" is "Any | None"',
        'Type of "Foo().req" is "Any"',
    ]

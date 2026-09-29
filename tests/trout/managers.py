from typing import ClassVar, TypeVar

from django.db import models
from typing_extensions import Self, assert_type

_M = TypeVar("_M", bound=models.Model)


class LiveManager(models.Manager["Article"]):
    def live(self) -> models.QuerySet["Article"]:
        return self.filter(published=True)


class Article(models.Model):
    published = models.BooleanField()

    objects: ClassVar[LiveManager] = LiveManager()


class AuditManager(models.Manager[_M]):
    def audited(self) -> models.QuerySet[_M]:
        return self.all()


class AuditedBase(models.Model):
    objects: ClassVar[AuditManager[Self]] = AuditManager()

    class Meta:
        abstract = True


class Note(AuditedBase): ...


class Plain(models.Model): ...


def check_manager_overrides() -> None:
    # A model's own manager narrows Model.objects without an override conflict.
    assert_type(Article.objects.live(), models.QuerySet[Article])
    assert_type(Note.objects.audited(), models.QuerySet[Note])
    # Models without one get Django's default Manager, specialised to the model.
    assert_type(Plain.objects, models.Manager[Plain])
    assert_type(Plain.objects.get(), Plain)


class AbstractNoManager(models.Model):
    class Meta:
        abstract = True


class Concrete(AbstractNoManager):
    @classmethod
    def first_row(cls) -> Self:
        return cls.objects.get()


def get_one(model: type[_M]) -> _M:
    return model.objects.get()


def check_default_manager_access() -> None:
    assert_type(Concrete.objects, models.Manager[Concrete])
    assert_type(Concrete.first_row(), Concrete)
    assert_type(get_one(Plain), Plain)
    # Django's ManagerDescriptor raises on instance access.
    Plain().objects  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[unresolved-attribute]

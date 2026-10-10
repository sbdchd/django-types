import datetime
from collections.abc import AsyncIterator, Iterator
from typing import Any

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.manager import BaseManager, ManyToManyRelatedManager, RelatedManager
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from typing_extensions import assert_type


class Book(models.Model):
    pass


class Join(models.Model):
    pass


class BookQuerySet(models.QuerySet[Book]):
    def custom(self) -> int:
        return 1


def need_manager(manager: models.Manager[Book]) -> None: ...
def need_base(manager: BaseManager[Book]) -> None: ...
def need_related(manager: RelatedManager[Book]) -> None: ...
def need_many(manager: ManyToManyRelatedManager[Book, Join]) -> None: ...


def check_managers(
    manager: models.Manager[Book, BookQuerySet],
    related: RelatedManager[Book, BookQuerySet],
    many: ManyToManyRelatedManager[Book, Join, BookQuerySet],
    plain: RelatedManager[Book],
    default_many: ManyToManyRelatedManager[Book, Join],
    book: Book,
) -> None:
    need_manager(manager)
    need_base(manager)
    need_related(related)
    need_many(many)
    assert_type(manager.get_queryset(), BookQuerySet)
    assert_type(manager.all(), BookQuerySet)
    assert_type(manager.filter().custom(), int)
    assert_type(manager.extra(select={"x": "1"}), BookQuerySet)
    assert_type(manager.db_manager(), models.Manager[Book, BookQuerySet])
    assert_type(manager.get(), Book)
    assert_type(manager.first(), Book | None)
    assert_type(manager.iterator(), Iterator[Book])
    assert_type(manager.aiterator(), AsyncIterator[Book])
    assert_type(manager.values().get(), dict[str, Any])
    assert_type(manager.dates("created", "year").first(), datetime.date | None)
    assert_type(manager.datetimes("created", "year").first(), datetime.datetime | None)
    assert_type(related.all(), BookQuerySet)
    assert_type(many.all().custom(), int)
    assert_type(plain.all(), models.QuerySet[Book])
    assert_type(default_many.all(), models.QuerySet[Book])
    # Django switches to the named manager's class, so the custom queryset is not preserved.
    assert_type(related(manager="other").all(), models.QuerySet[Book])
    assert_type(many(manager="other").all(), models.QuerySet[Book])
    related.add(book)
    related.set([book])
    many.add(book)
    many.set([book])
    assert_type(ContentType.objects.filter(), models.QuerySet[ContentType])
    assert_type(Book._default_manager.filter(), models.QuerySet[Book])
    ModelChoiceField(queryset=manager)
    ModelMultipleChoiceField(queryset=manager)


async def check_async_managers(
    manager: models.Manager[Book, BookQuerySet],
    related: RelatedManager[Book, BookQuerySet],
    book: Book,
) -> None:
    assert_type(await manager.aget(), Book)
    assert_type(await manager.afirst(), Book | None)
    assert_type(await manager.acount(), int)
    await related.aadd(book)
    await related.aset([book])


def check_auth_relations(group: Group, permission: Permission) -> None:
    assert_type(group.permissions.all(), models.QuerySet[Permission])
    assert_type(permission.group_set.all(), models.QuerySet[Group])
    assert_type(User.objects.with_perm("auth.change_user"), models.QuerySet[User])


# Managers are not querysets: Django does not copy these members onto them.
def check_queryset_only_members(manager: models.Manager[Book], qs: models.QuerySet[Book]) -> None:
    for _item in manager:  # type: ignore[attr-defined]  # pyright: ignore[reportGeneralTypeIssues]  # ty: ignore[not-iterable]
        pass
    len(manager)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
    manager[0]  # type: ignore[index]  # pyright: ignore[reportIndexIssue]  # ty: ignore[not-subscriptable]
    manager.delete()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[unresolved-attribute]
    manager.query  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[unresolved-attribute]
    _ = manager & qs  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]  # ty: ignore[unsupported-operator]

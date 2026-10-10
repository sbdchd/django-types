from django.db import models
from django.db.models import Prefetch
from typing_extensions import assert_type


class Book(models.Model): ...


class BookQuerySet(models.QuerySet[Book]):
    def published(self) -> "BookQuerySet":
        return self.filter(published=True)


def valid_prefetch(queryset: BookQuerySet, manager: models.Manager[Book, BookQuerySet]) -> None:
    prefetch: Prefetch[Book] = Prefetch("books", queryset=queryset)
    assert_type(queryset.prefetch_related(), BookQuerySet)
    assert_type(queryset.prefetch_related("authors", prefetch), BookQuerySet)
    assert_type(queryset.prefetch_related(None), BookQuerySet)
    assert_type(manager.prefetch_related("authors", prefetch), BookQuerySet)
    assert_type(manager.prefetch_related(None).published(), BookQuerySet)


def invalid_prefetch(queryset: BookQuerySet, manager: models.Manager[Book, BookQuerySet]) -> None:
    queryset.prefetch_related(1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[no-matching-overload]
    manager.prefetch_related(1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[no-matching-overload]
    queryset.prefetch_related(None, "authors")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[invalid-argument-type]
    manager.prefetch_related("authors", None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[invalid-argument-type]

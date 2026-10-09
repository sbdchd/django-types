from typing_extensions import assert_type

from django.db import models


class BookQuerySet(models.QuerySet["Book"]):
    def published(self) -> "BookQuerySet":
        return self.filter(published=True)


class BookManager(models.Manager["Book", BookQuerySet]):
    _queryset_class = BookQuerySet


class Book(models.Model):
    published = models.BooleanField()

    books = BookManager()
    generated_books = BookQuerySet.as_manager()


class Author(models.Model):
    name = models.CharField(max_length=100)


def chain_calls_return_the_queryset() -> None:
    assert_type(Author.objects.filter(), models.QuerySet[Author])
    assert_type(Author.objects.all().first(), Author | None)
    assert_type(Book.books.get_queryset(), BookQuerySet)
    assert_type(Book.books.filter(), BookQuerySet)
    assert_type(Book.books.order_by("pk").published(), BookQuerySet)
    assert_type(Book.books.select_related(None), BookQuerySet)
    assert_type(Book.books.get(pk=1), Book)


def count_rows(manager: models.Manager[Book]) -> int:
    return manager.count()


def custom_queryset_manager_is_still_a_manager() -> None:
    # The queryset parameter is covariant, so a narrower queryset still fits Manager[Book].
    count_rows(Book.books)


def as_manager_preserves_the_queryset_type() -> None:
    assert_type(Book.generated_books, models.Manager[Book, BookQuerySet])
    assert_type(Book.generated_books.get_queryset(), BookQuerySet)
    assert_type(Book.generated_books.all(), BookQuerySet)
    assert_type(Book.generated_books.filter().published(), BookQuerySet)
    assert_type(Book.generated_books.get(pk=1), Book)
    count_rows(Book.generated_books)

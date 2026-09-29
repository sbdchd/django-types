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

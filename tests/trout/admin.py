from collections.abc import Callable

from django.contrib import admin
from django.contrib.admin.filters import EmptyFieldListFilter
from django.db.models import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponseBase

from .models import IndexModel


@admin.register(IndexModel)
class IndexModelAdmin(admin.ModelAdmin[IndexModel]):
    list_display = [
        "pub_date",
        "title",
        "author",
        "height",
        "weight",
    ]
    list_filter = [
        ("author", EmptyFieldListFilter),
        "pub_date",
    ]


class ActionsAdmin(admin.ModelAdmin[IndexModel]):
    @admin.action(description="Archive")
    def archive(self, request: HttpRequest, queryset: QuerySet[IndexModel]) -> None: ...

    def get_actions(self, request: HttpRequest) -> dict[str, tuple[Callable[..., HttpResponseBase | None], str, str]]:
        # An action returning None (Django's usual) goes into the actions map.
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        actions["archive"] = (ActionsAdmin.archive, "archive", "Archive")
        return actions

from django.contrib import admin
from django.contrib.admin.filters import EmptyFieldListFilter

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

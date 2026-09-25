from django.db import models
from typing_extensions import assert_type


class Status(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class Priority(models.IntegerChoices):
    LOW = 1, "Low"
    HIGH = 2, "High"


class ChoiceModel(models.Model):
    # Leave default unset so only the enum class can guide choices inference.
    status = models.CharField(max_length=16, choices=Status)
    nullable_status = models.CharField(max_length=16, choices=Status, null=True)
    text = models.TextField(choices=Status)
    nullable_text = models.TextField(choices=Status, null=True)
    priority = models.IntegerField(choices=Priority)
    nullable_priority = models.IntegerField(choices=Priority, null=True)
    big_priority = models.BigIntegerField(choices=Priority)
    nullable_big_priority = models.BigIntegerField(choices=Priority, null=True)
    default_status = models.CharField(max_length=16, choices=Status, default=Status.DRAFT)
    default_priority = models.IntegerField(choices=Priority, default=Priority.LOW)


def check_choice_field_types(instance: ChoiceModel) -> None:
    assert_type(instance.status, str)
    assert_type(instance.nullable_status, str | None)
    assert_type(instance.text, str)
    assert_type(instance.nullable_text, str | None)
    assert_type(instance.priority, int)
    assert_type(instance.nullable_priority, int | None)
    assert_type(instance.big_priority, int)
    assert_type(instance.nullable_big_priority, int | None)
    assert_type(instance.default_status, str)
    assert_type(instance.default_priority, int)


def reject_mismatched_choice_enums() -> None:
    models.IntegerField(choices=Status)  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
    models.CharField(max_length=16, choices=Priority)  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]

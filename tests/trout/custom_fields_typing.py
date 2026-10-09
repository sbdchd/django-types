from django.db import models
from typing_extensions import assert_type


class CustomCharField(models.CharField):
    pass


class CustomIntegerField(models.IntegerField):
    pass


class CustomFieldModel(models.Model):
    nullable_char_default = CustomCharField(max_length=16, null=True, default=None)
    nullable_char_db_default = CustomCharField(max_length=16, null=True, db_default=None)
    nullable_integer_default = CustomIntegerField(null=True, default=None)
    nullable_integer_db_default = CustomIntegerField(null=True, db_default=None)


def check_custom_field_types(instance: CustomFieldModel) -> None:
    assert_type(instance.nullable_char_default, str | None)
    assert_type(instance.nullable_char_db_default, str | None)
    assert_type(instance.nullable_integer_default, int | None)
    assert_type(instance.nullable_integer_db_default, int | None)

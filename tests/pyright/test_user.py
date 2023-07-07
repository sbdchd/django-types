from .base import Result, run_pyright

def test_user_manager_specialises_to_self():
    results = run_pyright(
        """\
from django.db import models
from django.contrib.auth import models as auth_models

class MyUser(auth_models.User):
    age = models.IntegerField()

u = MyUser()
reveal_type(u.objects)
"""
        )

    assert results == [
        Result(
            type="information",
            message='Type of "u.objects" is "UserManager[MyUser]"',
            line=8,
            column=13,
        ),
    ]

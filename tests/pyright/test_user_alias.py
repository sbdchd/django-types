from .base import run_pyright


def test_user_alias_is_importable() -> None:
    """djangorestframework-stubs types Request.user as `_User | AnonymousUser`."""
    results = run_pyright(
        """\
from django.contrib.auth.models import AbstractUser, AnonymousUser, _User

def name(user: _User | AnonymousUser) -> str:
    return user.get_username()

def concrete(user: _User) -> AbstractUser:
    return user
"""
    )
    assert [r for r in results if r.type == "error"] == []

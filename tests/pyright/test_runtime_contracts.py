from .base import run_pyright


def test_supported_runtime_contracts() -> None:
    assert (
        run_pyright(
            """
from datetime import timedelta
from typing_extensions import assert_type
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.base import SessionBase
from django.core.management.color import Style
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.models import Model
from django.db.models.manager import ManyToManyRelatedManager
from django.http import HttpRequest

class Target(Model):
    pass

class Through(Model):
    pass

async def supported(
    manager: ManyToManyRelatedManager[Target, Through], target: Target,
    session: SessionBase, request: HttpRequest, user: AbstractBaseUser,
    database: BaseDatabaseWrapper, style: Style,
) -> None:
    manager.add(target, 1)
    await manager.aadd(target, 2)
    manager.remove(target, 1)
    await manager.aremove(target, 2)
    manager.set([target, 1])
    await manager.aset([target, 2])
    session.set_expiry(timedelta(days=1))
    await session.aset_expiry(timedelta(days=1))
    assert_type(session.key_salt, str)
    request.user = user
    assert_type(await request.auser(), AbstractBaseUser | AnonymousUser)
    database.inc_thread_sharing()
    database.dec_thread_sharing()
    operations = BaseDatabaseOperations(database)
    assert_type(operations.quote_name("table"), str)
    statements = operations.sql_flush(style, ["table"], reset_sequences=True)
    assert_type(statements, list[str])
    operations.execute_sql_flush(statements)
    assert_type(operations.sequence_reset_sql(style, [Target]), list[str])
"""
        )
        == []
    )


def test_rejects_incompatible_models_and_users() -> None:
    results = run_pyright(
        """
from django.http import HttpRequest
from django.db.models import Model
from django.db.models.manager import ManyToManyRelatedManager

class Target(Model):
    pass

class Through(Model):
    pass

async def invalid(manager: ManyToManyRelatedManager[Target, Through], through: Through, request: HttpRequest) -> None:
    manager.add(through)
    await manager.aset([through])
    request.user = object()
"""
    )
    assert len(results) == 3
    assert all(result.type == "error" for result in results)


def test_permissions_accept_backend_policy_objects() -> None:
    assert (
        run_pyright(
            """
from dataclasses import dataclass
from typing import Protocol
from typing_extensions import assert_type
from django.contrib.auth.models import AbstractUser

@dataclass
class Policy:
    project_id: int

class PermissionActor(Protocol):
    def has_perm(self, perm: str, obj: object | None = None) -> bool: ...

async def check(user: AbstractUser, policy: Policy) -> None:
    actor: PermissionActor = user
    assert_type(actor.has_perm("project.view", policy), bool)
    assert_type(user.has_perms(["project.view"], policy), bool)
    assert_type(await user.ahas_perm("project.view", policy), bool)
    assert_type(await user.ahas_perms(["project.view"], policy), bool)
"""
        )
        == []
    )


def test_inline_and_staticfiles_runtime_contracts() -> None:
    assert (
        run_pyright(
            """
from types import ModuleType
from typing_extensions import assert_type
from asgiref.typing import ASGI3Application
from django.contrib.admin import AdminSite, TabularInline
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler, StaticFilesHandler
from django.core.handlers.wsgi import WSGIHandler
from django.db.models import Model
from django.forms import BaseFormSet, Form
from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.urls import resolve

class Parent(Model): pass
class Child(Model): pass
class ChildInline(TabularInline[Child, Parent]):
    model = Child

async def check(request: HttpRequest, parent: Parent, app: ASGI3Application,
                wsgi: WSGIHandler, urls: ModuleType, forms: BaseFormSet[Form]) -> None:
    inline = ChildInline(Parent, AdminSite())
    formset = inline.get_formset(request, obj=parent)
    assert "name" not in formset().form.base_fields
    assert_type(forms.form, type[Form])
    resolve('/example/', urlconf=urls)
    assert_type(await ASGIStaticFilesHandler(app).get_response_async(request), HttpResponseBase)
    assert_type(StaticFilesHandler(wsgi).serve(request), HttpResponseBase)
"""
        )
        == []
    )

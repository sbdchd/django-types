from .base import run_pyright


def test_supported_runtime_contracts() -> None:
    assert run_pyright(
        '''
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
'''
    ) == []


def test_rejects_incompatible_models_and_users() -> None:
    results = run_pyright(
        '''
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
'''
    )
    assert len(results) == 3
    assert all(result.type == "error" for result in results)

import pytest
from pydantic import ValidationError
from unittest.mock import AsyncMock, MagicMock

from app.services.user import UserService
from app.services.auth import AuthService
from app.schemas.user import UserUpdate


@pytest.mark.asyncio
async def test_update_only_changes_provided_fields():
    existing = MagicMock()
    existing.name = "Old Name"
    existing.password = "old_hash"

    service = UserService(AsyncMock())
    service.get_user_by_id = AsyncMock(return_value=existing)
    service.log = MagicMock()

    result = await service.update_user(1, UserUpdate(name="New Name"))

    assert result.name == "New Name"
    assert result.password == "old_hash"


@pytest.mark.asyncio
async def test_update_rehashes_new_password():
    existing = MagicMock()
    existing.password = "old_hash"

    service = UserService(AsyncMock())
    service.get_user_by_id = AsyncMock(return_value=existing)
    service.log = MagicMock()

    await service.update_user(1, UserUpdate(password="newpass"))

    assert existing.password != "newpass"
    assert existing.password != "old_hash"


@pytest.mark.asyncio
async def test_update_missing_user_returns_none():
    service = UserService(AsyncMock())
    service.get_user_by_id = AsyncMock(return_value=None)

    result = await service.update_user(999, UserUpdate(name="X"))
    assert result is None


def test_user_update_rejects_email():
    # email не входить у дозволені поля -> extra="forbid" має відхилити запит
    with pytest.raises(ValidationError):
        UserUpdate(email="new@gmail.com")


def test_user_update_rejects_is_active():
    with pytest.raises(ValidationError):
        UserUpdate(is_active=False)


def test_user_update_rejects_blank_name():
    with pytest.raises(ValidationError):
        UserUpdate(name="   ")


@pytest.mark.asyncio
async def test_authenticate_returns_none_for_wrong_password():
    from app.utils.password import hash_password

    user = MagicMock()
    user.password = hash_password("correctpass")

    service = AuthService(AsyncMock())
    service.get_user_by_email = AsyncMock(return_value=user)

    result = await service.authenticate("test@gmail.com", "wrongpass")
    assert result is None


@pytest.mark.asyncio
async def test_authenticate_returns_none_for_unknown_email():
    service = AuthService(AsyncMock())
    service.get_user_by_email = AsyncMock(return_value=None)

    result = await service.authenticate("nobody@gmail.com", "anypass")
    assert result is None


@pytest.mark.asyncio
async def test_authenticate_returns_user_for_correct_credentials():
    from app.utils.password import hash_password

    user = MagicMock()
    user.password = hash_password("secret")

    service = AuthService(AsyncMock())
    service.get_user_by_email = AsyncMock(return_value=user)
    service.log = MagicMock()

    result = await service.authenticate("test@gmail.com", "secret")
    assert result is user

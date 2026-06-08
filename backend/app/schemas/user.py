from pydantic import BaseModel, field_validator

from app.utils.validators import validate_email


class User(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class SignInRequest(BaseModel):
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str) -> str:
        return validate_email(value)


class SignUpRequest(BaseModel):
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str) -> str:
        return validate_email(value)


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str | None) -> str | None:
        if value is None:
            return value
        return validate_email(value)


class UserDetail(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UsersList(BaseModel):
    users: list[UserDetail]
    total: int
    offset: int
    limit: int

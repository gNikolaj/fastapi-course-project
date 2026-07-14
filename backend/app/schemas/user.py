from pydantic import BaseModel, ConfigDict, field_validator

from app.utils.validators import validate_email


class User(BaseModel):
    id: int
    name: str | None = None
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
    model_config = ConfigDict(extra="forbid")

    name: str | None = None
    password: str | None = None

    @field_validator("name")
    @classmethod
    def name_validator(cls, value: str | None) -> str | None:
        if value is None:
            return value
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        return value


class UserDetail(BaseModel):
    id: int
    name: str | None = None
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UsersList(BaseModel):
    users: list[UserDetail]
    total: int
    offset: int
    limit: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

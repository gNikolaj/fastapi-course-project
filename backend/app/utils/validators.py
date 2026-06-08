import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email(value: str) -> str:
    if not EMAIL_REGEX.match(value):
        raise ValueError("Invalid email format")
    return value.lower()

from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError("account_id must be positive")
        return value


user = User(
    name="Ali",
    email="ali@gmail.com",
    account_id=100
)

# Convertir en JSON string
json_str = user.model_dump_json()
print(json_str)

# Convertir en dictionnaire
json_dict = user.model_dump()
print(json_dict)

print(user)
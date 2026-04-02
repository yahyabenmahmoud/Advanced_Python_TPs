from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int

# Ceci fonctionne même si c'est faux
user = User(
    name="Ali",
    email="ali",
    account_id="hello"
)

print(user)
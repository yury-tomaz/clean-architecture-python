# test_user.py
import uuid
from src.domain.entities.user_entity import User

def test_user_creation():
    user = User(name="Alice", email="alice@example.com", password="password123")
    assert isinstance(user.id, uuid.UUID)
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.password == "password123"
    assert user.is_active is True

def test_user_creation_with_custom_id():
    custom_id = uuid.uuid4()
    user = User(id=custom_id, name="Bob", email="bob@example.com", password="password456")
    assert user.id == custom_id
    assert user.name == "Bob"
    assert user.email == "bob@example.com"
    assert user.password == "password456"
    assert user.is_active is True

import uuid

class User:
    def __init__(self, id=None, name='', email='', password='', is_active=True):
        # Se o id não for fornecido, gera um novo UUID
        self.id = id if id is not None else uuid.uuid4()
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active

    def __repr__(self):
        return (f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, "
                f"password={self.password!r}, is_active={self.is_active!r})")

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.name == other.name and
                    self.email == other.email and
                    self.password == other.password and
                    self.is_active == other.is_active)
        return False

    def __hash__(self):
        return hash((self.id, self.name, self.email, self.password, self.is_active))

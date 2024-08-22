import uuid

class Task:
    def __init__(self, id=None, user_id='', title='', description='', is_completed=False):
        # Se o id não for fornecido, gera um novo UUID
        self.id = id if id is not None else uuid.uuid4()
        self.title = title
        self.description = description
        self.is_completed = is_completed 
        self.user_id = user_id
        
    def __repr__(self):
        return (f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r},"
                f"is_completed={self.is_completed!r})")

    def __eq__(self, other):
           
        if isinstance(other, Task):
            return ( self.id == other.id and
            self.user_id == other.user_id and
            self.title == other.title and
            self.description == other.description and
            self.is_completed == other.is_completed)
        return False

    def __hash__(self):
        return hash((self.id, self.user_id, self.title, self.description, self.is_completed))

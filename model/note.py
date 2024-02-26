from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4, UUID


@dataclass
class Note:
    id: UUID
    date_create: datetime
    date_modify: datetime
    text: str
    def __init__(self, text):
        self.id = uuid4()
        self.date_create = datetime.now()
        self.date_modify = datetime.now()
        self.text = text

    def __str__(self):
        return (f"'id': {self.id}, 'date_create': {self.date_create}, 'date_modify': {self.date_modify}, "
                f"'text': {self.text}")

    def __hash__(self):
        return hash(str(self.id) + str(self.date_create))
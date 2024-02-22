from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: str
    date_create: datetime
    date_modify: datetime
    text: str

    def __str__(self):
        return f"'id': {self.id}, 'date_create': {self.date_create}, 'date_modify': {self.date_modify}, 'text': {self.text}"

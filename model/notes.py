from datetime import datetime

from model.note import Note
from dataclasses import dataclass


@dataclass
class Notes:

    notes: dict[datetime, list[Note]]

    def get_notes(self):
        pass

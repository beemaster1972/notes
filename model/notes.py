from datetime import datetime, date
from uuid import UUID

from model.note import Note
from dataclasses import dataclass


@dataclass
class Notes:
    notes: dict[date, dict[UUID, Note]]

    def get_notes(self, filter: any = None):
        if filter is None:
            return self.notes
        return {k:v for k,v in self.notes if filter(k,v)}

    @staticmethod
    def validate_key(key: date):
        if type(key) not in (date, datetime):
            raise KeyError(f"Ключ {key} должен быть датой")

    def __getitem__(self, item):
        self.validate_key(item)
        return self.notes[item]

    def __setitem__(self, key: date, value: Note):
        self.validate_key(key)
        if not isinstance(value, Note):
            raise ValueError(f"Переданное значение {value} не является заметкой")
        self.notes[key] = self.notes.get(key, {}).update({value.id: value})

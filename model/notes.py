from datetime import datetime, date
from uuid import UUID

from model.note import Note


class Notes:
    notes: dict[date, dict[UUID, Note]]
    def __init__(self, notes: dict = None):
        if notes is None:
            notes = {}
        self.notes = notes

    def get_notes(self, filter_notes: any = None, key_name: str = '_Note__date_create', condition: any = None):
        if filter_notes is None:
            return self.notes
        return {k: v for k, v in self.notes if filter_notes(key_name, v, condition)}

    @staticmethod
    def validate_key(key: date):
        if type(key) not in (date, datetime):
            raise KeyError(f"Ключ {key} должен быть датой")

    def __getitem__(self, item):
        self.validate_key(item)
        return self.notes.get(item, {})

    def __setitem__(self, key: date, value: Note):
        self.validate_key(key)
        if not isinstance(value, Note):
            raise ValueError(f"Переданное значение {value} не является заметкой")
        self.notes.setdefault(key, {}).update({value.id: value})


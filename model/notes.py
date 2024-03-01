from datetime import datetime, date

from model.note import Note


class Notes:

    def __init__(self, notes: dict = None):
        self.notes = {}
        if notes is not None:
            for date_notes, notes_dict in notes.items():
                temp = {}
                for note_id, note in notes_dict.items():
                    temp[note_id] = Note(**note)
                if len(temp):
                    self.notes[date_notes] = temp

    def get_notes(self, filter_notes: any = None, condition: any = None):
        if filter_notes is None or condition is None:
            return self.notes
        return {k: v for k, v in self.notes if filter_notes(condition)}

    @staticmethod
    def validate_key(key: str):
        if type(key) not in (str,):
            raise KeyError(f"Ключ {key} должен быть строкой")

    def __getitem__(self, item):
        self.validate_key(item)
        return self.notes.get(item, {})

    def __setitem__(self, key: str, value: Note):
        self.validate_key(key)
        if not isinstance(value, Note):
            raise ValueError(f"Переданное значение {value} не является заметкой")
        self.notes.setdefault(key, {}).update({value.id: value})

from datetime import date

from model.note import Note
from model.notes import Notes


class Viewer:

    def __init__(self, notes: Notes):
        self.notes = notes

    @staticmethod
    def filter_note(key_name, value: Note, condition=None):
        if condition is None:
            return True
        return value[key_name] == condition

    def view_notes_by_date_create(self, date_filter: date = None):
        if date_filter is None:
            return self.notes.notes
        views = sorted(
            self.notes.get_notes(self.filter_note, key_name='_Note__date_create', condition=date_filter).values(),
            key=lambda note: note.date_create)
        return views

    def view_notes_by_date_modify(self, date_filter: date = None):
        views = sorted(self.notes.get_notes(self.filter_note, key_name='_date_modify', condition=date_filter).values(),
                       key=lambda note: note.date_modify)
        return views

    def view_notes_by_title(self, title: str = None):
        views = sorted(self.notes.get_notes(self.filter_note, key_name='_title', condition=title).values(),
                       key=lambda note: note.title)
        return views

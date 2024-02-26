from datetime import date

from model.notes import Notes


class Viewer:

    def __init__(self, notes: Notes):
        self.notes = notes

    @staticmethod
    def filter_note(key, value):
        pass

    def view_notes_by_date_create(self, date_filter: date):
        views = sorted(self.notes.get_notes(self.filter_note).values(), key=lambda note: note.date_create)

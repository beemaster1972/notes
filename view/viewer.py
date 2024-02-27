from datetime import date

from model.note import Note
from model.notes import Notes


class Viewer:

    def __init__(self, notes: Notes):
        self.notes = notes

    @staticmethod
    def filter_note(condition=None):
        if condition is None:
            return True
        return all(condition)

    def view_notes(self, condition=None):
        views = self.notes.get_notes(self.filter_note, condition=condition)
        return views



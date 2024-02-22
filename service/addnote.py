from model import notes
from model import note


class AddNote(note, notes):

    def __init__(self, notes_store: notes):
        self.notes = notes_store

    def add_note(self, new_note: note) -> None:
        """

        :param new_note:
        :type new_note:
        """
        pass

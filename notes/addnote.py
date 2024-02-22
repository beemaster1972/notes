import notes
import note


class AddNote(notes, note):

    def __init__(self, notes_store: notes):
        self.notes = notes_store
    def add_note(self, new_note: note) -> None:
        """

        :param new_note:
        :type new_note:
        """
        pass

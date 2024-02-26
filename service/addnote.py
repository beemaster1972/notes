from model.notes import Notes
from model.note import Note
from operation import Operation


class AddNote(Operation):

    def __init__(self, notes: Notes):
        self.notes = notes

    def operation(self, note: Note) -> None:
        """
        Метод добавления новой заметки
        :param note: заметка
        :type Note:
        """
        self.notes[note.date_create.date()] = self.notes.notes.get(note.date_create.date(), {}).update(
            {note.id: note})

from model.note import Note
from model.notes import Notes
from service.notesoperation import Operation


class DeleteNote(Operation):
    def __init__(self, notes: Notes):
        self.notes = notes

    def operation(self, note: Note) -> Note:
        """
        Метод удаляющий заметку
        :param note: заметка для удаления
        :type note: Note
        :return: удаленную заметку
        :rtype: Note
        """
        notes_dict = self.notes[note.date_create.date()]
        return notes_dict.popitem(note.id)

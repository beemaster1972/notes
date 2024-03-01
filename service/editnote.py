from datetime import datetime

from model.note import Note
from model.notes import Notes
from service.notesoperation import Operation
from service.textedit import TextEdit


class EditNote(Operation):

    def __init__(self, notes: Notes):
        self.notes = notes

    def operation(self, note: Note) -> (Note,):
        """
        Метод редактирующий заметку
        :param note: заметка для редактирования
        :type Note:
        :return: кортеж отредактированную заметку и словарь заметок
        :rtype: Note
        """
        note = TextEdit().edit_note(note)
        note.date_modify = datetime.now()
        self.notes[str(note.date_create.date())] = note
        return note, self.notes

from model.note import Note
from service.notesoperation import Operation


class EditNote(Operation):
    def operation(self, note: Note) -> Note:
        """
        Метод редактирующий заметку
        :param note: заметка для редактирования
        :type Note:
        :return: отредактированную заметку
        :rtype: Note
        """

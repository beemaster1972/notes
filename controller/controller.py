from service.addnote import AddNote
from service.deletenote import DeleteNote
from service.editnote import EditNote
from service.loadnotes import LoadNotes
from service.nulloperation import NullOperation
from service.savenotes import SaveNotes
from service.textedit import TextEdit
from view.viewer import *
from model.notes import Notes
from curses import wrapper
import os


class Controller:
    __PROMPT = ['1. Создать заметку',
                '2. Редактировать заметку',
                '3. Удалить заметку',
                '4. Показать заметки',
                '5. Сохранить заметки в файл',
                '6. Загрузить заметки из файла',
                '0. Выход']
    __MENU_COMMAND = {'1': 'add',
                      '2': 'edit',
                      '3': 'delete',
                      '4': 'list',
                      '5': 'save',
                      '6': 'load',
                      '0': 'exit'}

    def __init__(self):
        self.notes = Notes(LoadNotes("notes.json").load())
        self.viewer = Viewer(self.notes)
        self.__operations = {'add': AddNote(self.notes),
                             'delete': DeleteNote(self.notes),
                             'edit': EditNote(self.notes)}

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        command = ''
        while (command != 'exit'):
            print('\n'.join(self.__PROMPT))
            command = self.__MENU_COMMAND.get(input("Ваш выбор: "), '_')
            match (command):
                case 'add' | 'edit' | 'delete':
                    if command == 'add':
                        note = TextEdit().edit_note()
                    else:
                        note = self.viewer.get_note_with_command()
                    n, self.notes = self.__operations.get(command, NullOperation()).operation(note)
                    self.viewer.update_notes(self.notes)
                case 'save':
                    SaveNotes('notes.json').save(self.notes)
                case 'list':
                    note = wrapper(self.viewer.get_note_with_command())
                case 'exit':
                    print('Всего хорошего! Приложение закрывается')
                    print('Сохранение заметок...')
                    SaveNotes('notes.json').save(self.notes)
                    print('Всё удачно! До, свидания!')
                case _:
                    print("Не распознанная команда")

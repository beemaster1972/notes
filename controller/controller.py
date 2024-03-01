from service.addnote import AddNote
from service.deletenote import DeleteNote
from service.editnote import EditNote
from service.loadnotes import LoadNotes
from service.nulloperation import NullOperation
from service.savenotes import SaveNotes
from view.viewer import *
from model.notes import Notes
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
                             'edit': EditNote()}

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        command = ''
        while (command != 'exit'):
            print('\n'.join(self.__PROMPT))
            command = self.__MENU_COMMAND.get(input("Ваш выбор: "), '_')
            match (command):
                case 'add' | 'edit' | 'delete':
                    note = Note(title="Новая заметка", text=['String1', 'String2', 'String3'])
                    self.__operations.get(command, NullOperation()).operation(note)
                case 'save':
                    SaveNotes('notes.json').save(self.notes)
                case 'list':
                    for date_notes, notes in self.viewer.view_notes().items():
                        if type(notes) is dict:
                            for id_note, note in notes.items():
                                print(f'{date_notes} {note}')
                case 'exit':
                    print('Всего хорошего! Приложение закрывается')
                    print('Сохранение заметок...')
                    SaveNotes('notes.json').save(self.notes)
                    print('Всё удачно! До, свидания!')
                case _:
                    print("Не распознанная команда")

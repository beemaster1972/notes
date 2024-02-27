import json
import os


class LoadNotes:
    __FILE_NOT_EXIST = False

    def __init__(self, file_name):
        if not os.path.exists(file_name):
            print(f"Файл {file_name} не существует. Загрузка не возможна!")
            self.__FILE_NOT_EXIST = True
        else:
            self.__file_name = file_name

    def load(self):
        if not self.__FILE_NOT_EXIST:
            with open(self.__file_name, 'r') as file:
                return json.load(file)

    def __call__(self, *args, **kwargs):
        return self.load()

from datetime import datetime
from uuid import uuid4, UUID


class Note:

    def __init__(self, title="", text=None):
        self.__id = uuid4()
        self.__date_create = datetime.now()
        self._date_modify = datetime.now()
        self._title = title
        if text is None:
            self._text = []
        self._text = text

    @property
    def id(self):
        return self.__id

    @property
    def date_create(self):
        return self.__date_create

    @property
    def date_modify(self):
        return self._date_modify

    @date_modify.setter
    def date_modify(self, value):
        self._date_modify = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __setattr__(self, key, value):

        if 'date' in key :
            if not isinstance(value, datetime):
                raise ValueError(f"Значение даты: {value}, не валидно")
        elif key == '_title':
            if not isinstance(value, str):
                raise ValueError(f'Значение загаловка: {value}, не строка!')
        elif key == '_text':
            if not isinstance(value, list):
                raise ValueError(f'Текст заметки: {value}, не является списком')
        object.__setattr__(self, key, value)

    def __getitem__(self, item):
        if item not in self.__dict__:
            raise IndexError(f"Нет такого атрибута: {item} у класса Note")
        return self.__dict__[item]

    def __str__(self):
        return (f"'id': {self.id}, 'date_create': {self.date_create}, 'date_modify': {self.date_modify}, "
                f"'title': {self.title}, 'text': {self.text}")

    def __hash__(self):
        return hash(str(self.id) + str(self.date_create) + str(self.title))

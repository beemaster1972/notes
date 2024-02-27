import json
import os

from model.notes import Notes


class SaveNotes:

    def __init__(self, file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                json.dump({}, file, indent=4)
        else:
            self.__file_name = file_name

    def save(self, notes: Notes, append: bool = False):
        if append:
            parameter = 'w+'
        else:
            parameter = 'w'
        notes_for_serialized = {}
        for date_notes, dict_notes in notes.notes.items():
            save_dump = {k: v() for k, v in dict_notes.items()}
            notes_for_serialized[date_notes] = save_dump
        with open(self.__file_name, parameter) as file:
            json.dump(notes_for_serialized, file, indent=4)

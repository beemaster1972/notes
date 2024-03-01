from datetime import date

from model.note import Note
from model.notes import Notes
import curses
from curses import wrapper


class Viewer:

    def __init__(self, notes: Notes):
        self.notes = notes

    @staticmethod
    def filter_note(condition=None):
        if condition is None:
            return True
        return all(condition)

    def view_notes(self, condition=None):
        views = self.notes.get_notes(self.filter_note, condition=condition)
        return views

    def get_note_with_command(self, condition=None):
        notes_select = curses.initscr()
        selected_notes = self.notes.get_notes(self.filter_note, condition)
        list_notes = []
        for notes_date, notes in selected_notes:
            for id_note, note in notes:
                list_notes.append(note)
                notes_select.addstr(note.date_create + " " + note.title)
        exit_from_cycle = False
        current_index = 0
        while not exit:
            notes_select.refresh()
            command = notes_select.getkey()
            match command:
                case curses.KEY_ENTER:
                    exit_from_cycle = True
                case curses.KEY_UP:
                    current_index -= 1 if current_index > 0 else

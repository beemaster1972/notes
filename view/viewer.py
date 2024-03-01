from datetime import date

from model.note import Note
from model.notes import Notes
import curses


class Viewer:

    def __init__(self, notes: Notes):
        self.notes = notes

    @staticmethod
    def filter_note(condition=None):
        if condition is None:
            return True
        return all(condition)

    def get_note_with_command(self, condition=None) -> Note | None:
        def set_attr(scr: curses.window, ind: int, string: str, attribute: int) -> None:
            scr.addstr(ind, 0, string, attribute)

        notes_select = curses.initscr()
        notes_select.keypad(True)
        curses.curs_set(False)
        curses.cbreak()
        notes_select.clear()
        notes_select.refresh()
        selected_notes = self.notes.get_notes(self.filter_note, condition)
        list_notes = []
        for notes_date, notes in selected_notes.items():
            for i, note in enumerate(notes.values()):
                list_notes.append(note)
                notes_select.addstr(i, 0, note.get_title_of_note())
        exit_from_cycle = not bool(len(list_notes))
        cancel = False
        current_index = 0
        while not exit_from_cycle:
            set_attr(notes_select, current_index, list_notes[current_index].get_title_of_note(), curses.A_REVERSE)
            notes_select.refresh()
            command = notes_select.getkey()
            # print()
            match command:
                case '\n':
                    exit_from_cycle = True
                case "KEY_UP":
                    set_attr(notes_select, current_index, list_notes[current_index].get_title_of_note(),
                             curses.A_NORMAL)
                    if current_index > 0:
                        current_index -= 1
                    else:
                        current_index = len(list_notes) - 1
                case "KEY_DOWN":
                    set_attr(notes_select, current_index, list_notes[current_index].get_title_of_note(),
                             curses.A_NORMAL)
                    if current_index < len(list_notes) - 1:
                        current_index += 1
                    else:
                        current_index = 0
                case "^[" | "KEY_BACKSPACE" | "\x7f":
                    exit_from_cycle = True
                    cancel = True
                case _:
                    notes_select.addstr(20, 5, command, curses.A_REVERSE+curses.A_PROTECT)
        return list_notes[current_index] if len(list_notes) and not cancel else None

    def update_notes(self, notes):
        self.notes = notes

    @staticmethod
    def display_note(note: Note) -> None:
        if isinstance(note, Note):
            print(f"Дата создания: {note.date_create}\n" +
                  f"Дата модификации: {note.date_modify}\n" +
                  f"Заголовок: {note.title}\n" +
                  "Текст заметки:")
            print(*note.text, sep='\n')

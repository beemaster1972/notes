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

    def get_note_with_command(self, stdscr, condition=None) -> (Note, bool):
        def set_attr(scr: curses.window, ind: int, string: str, attribute: int) -> None:
            scr.addstr(ind + 1, 0, string, attribute)

        stdscr.erase()
        stdscr.clear()
        stdscr.refresh()
        selected_notes = self.notes.get_notes(self.filter_note, condition)
        list_notes = []
        set_attr(stdscr,
                 -1,
                 "ENTER - to select note  CTRL+X or ALT+C - to exit without choice",
                 curses.A_REVERSE)
        for notes_date, notes in selected_notes.items():
            for i, note in enumerate(notes.values()):
                list_notes.append(note)
        stdscr.erase()
        for i, note in enumerate(list_notes):
            set_attr(stdscr, i, note.get_title_of_note(), curses.A_NORMAL)
        exit_from_cycle = not bool(len(list_notes))
        cancel = False
        current_index = 0
        stdscr.refresh()
        while not exit_from_cycle:
            set_attr(stdscr, current_index, list_notes[current_index].get_title_of_note(), curses.A_REVERSE)
            stdscr.refresh()
            command = stdscr.getkey()
            match command:
                case '\n':
                    exit_from_cycle = True
                case "KEY_UP":
                    set_attr(stdscr, current_index, list_notes[current_index].get_title_of_note(),
                             curses.A_NORMAL)
                    if current_index > 0:
                        current_index -= 1
                    else:
                        current_index = len(list_notes) - 1
                case "KEY_DOWN":
                    set_attr(stdscr, current_index, list_notes[current_index].get_title_of_note(),
                             curses.A_NORMAL)
                    if current_index < len(list_notes) - 1:
                        current_index += 1
                    else:
                        current_index = 0
                case "ALT_C" | "^X":
                    exit_from_cycle = True
                    cancel = True
                case _:
                    pass
        return (cancel, list_notes[current_index]) if len(list_notes) else (cancel, Note())

    def update_notes(self, notes):
        self.notes = notes

    @staticmethod
    def display_note(note: Note) -> None:
        date_create = ""
        date_modify = ""
        title = ""
        text = ""
        match type(note) is Note:
            case True:
                date_create = note.date_create
                date_modify = note.date_modify
                title = note.title
                text = '\n'.join(note.text)
            case False:
                date_create = note[date_create]
                date_modify = note[date_modify]
                title = note[title]
                text = '\n'.join(note[text])
            case _:
                pass
        if isinstance(note, (Note, dict)):
            print(f"Дата создания: {date_create}\n" +
                  f"Дата модификации: {date_modify}\n" +
                  f"Заголовок: {title}\n" +
                  "Текст заметки:")
            print(text)

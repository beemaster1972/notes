import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from model.note import Note


class TextEdit:

    def __init__(self, note: Note = None):
        if note is None:
            self.note = Note()
        else:
            self.note = note

    def text_edit(self, stdscr: curses.window):
        # print(curses.LINES, curses.COLS)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(0, 0, "Ctrl+g to finish edit", curses.A_PROTECT + curses.A_REVERSE)
        stdscr.refresh()
        win = curses.newwin(11, 80, 2, 0)
        win.addstr(0, 0, self.note.title, curses.A_REVERSE)
        for i, string in enumerate(self.note.text):
            win.addstr(i + 1, 0, string, curses.A_NORMAL)
        box = Textbox(win, insert_mode=True)
        box.stripspaces = True
        box.edit()
        message = box.gather()
        stdscr.clear()
        stdscr.refresh()
        return message

    def edit_note(self, note: Note = None) -> Note:
        if note is None:
            self.note = Note()
        else:
            self.note = note

        text = wrapper(self.text_edit).split('\n')
        self.note.title = text[0]
        self.note.text = text[1:]
        return self.note


if __name__ == '__main__':
    text_edit = TextEdit()
    result = wrapper(text_edit.edit_note())
    print(result)

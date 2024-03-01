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
        curses.noecho()
        curses.curs_set(1)
        curses.nocbreak()
        stdscr.keypad(1)
        stdscr.clear()
        stdscr.refresh()
        win = curses.newwin(10, 80, 0, 0)
        win.addstr(0, 0, self.note.title, curses.A_REVERSE)
        for i, string in enumerate(self.note.text):
            win.addstr(i, 0, string, curses.A_NORMAL)
        box = Textbox(win)
        box.edit()
        message = box.gather()
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

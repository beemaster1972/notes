import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from model.note import Note


class TextEdit:

    def text_edit(self, stdscr: curses.window):
        curses.noecho()
        stdscr.keypad(1)
        stdscr.clear()
        stdscr.refresh()
        win = curses.newwin(10, 80, 0,0)
        win.addstr(0,0,self.note.title)
        box = Textbox(win)
        box.edit()
        message = box.gather()
        return message

    def edit_note(self, note:Note) -> Note:
        self.note = note



if __name__ == '__main__':
    text_edit = TextEdit()
    result = wrapper(text_edit.textedit)
    list_str = result.split('\n')
    print(type(result))
    print(len(result))
    print(list_str)

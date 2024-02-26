import curses
from curses import wrapper


class TextEdit:
    def __init__(self):
        self.screen = curses.initscr()

    def __del__(self):
        curses.endwin()

    def textedit(self,init_text):





if __name__ == '__main__':
    text_edit = TextEdit()
    curses.wrapper(text_edit.textedit)
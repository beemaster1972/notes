import curses
from curses import wrapper


class TextEdit:
    """
    Модуль для редактирования текста в консоли
    """

    def __init__(self):
        self.screen = curses.initscr()

    def __del__(self):
        curses.endwin()

    def textedit(self, init_text: str) -> str:
        """
        Основной метод
        :param init_text: Начальный текст
        :type init_text:
        :return: строку
        :rtype:
        """
        self.screen.addstr(init_text)
        while True:
            ch = self.screen.getkey()
            self.screen.addstr(ch)
            # init_text += ch
            self.screen.refresh()


if __name__ == '__main__':
    text_edit = TextEdit()
    curses.wrapper(text_edit.textedit)

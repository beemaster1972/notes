import curses
import os


if __name__ == '__main__':
    print(os.getenv("TERM"))
    screen = curses.initscr()
    screen = curses.newwin(80,80)
    if not screen:
        print("ХУЙНЯ")
    screen = curses.newwin(80, 80)
    screen.addstr(0, 0, "(0,0")
    screen.addstr(1, 1, "TEST")
    while True:
        screen.refresh()

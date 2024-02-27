import datetime

from model.note import Note
from model.notes import Notes
from controller.controller import Controller
import curses

from service import savenotes
from service.textedit import TextEdit

if __name__ == '__main__':
    Controller().run()

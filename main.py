import time

from PyQt5.uic.properties import QtWidgets
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
import speech_recognition as sr
import sys
import traceback
from convert_func import *

r = sr.Recognizer()


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.info_form = InfoForm(self)
        self.f_path = ''
        uic.loadUi('main_form.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Audio converter')
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.file_btn.clicked.connect(self.choose_file)
        self.convert_btn.clicked.connect(self.convert_qt)
        self.setFixedSize(850, 500)
        self.info_btn.clicked.connect(self.open_info_form)

    def choose_file(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Файл (*.wav);;')[0]
        self.f_path = (str(fname))

    def convert_qt(self):
        res = convert(self.f_path)
        self.res_space.setPlainText(str(res))

    def open_info_form(self):
        self.info_form.show()


class InfoForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        uic.loadUi('info_form.ui', self)
        self.label.setText('<a href="https://github.com/MishaSok">GitHub Account</a>')
        self.label.setOpenExternalLinks(True)
        self.label_2.setText('<a href="https://github.com/MishaSok/audio_converter_wav">GitHub Repository</a>')
        self.label_2.setOpenExternalLinks(True)

    def initUI(self, args):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Информация')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

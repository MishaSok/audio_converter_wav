from PyQt5.uic.properties import QtWidgets
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import speech_recognition as sr
import sys
import traceback

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
        self.f_path = ''
        uic.loadUi('lmao.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.file_btn.clicked.connect(self.choose_file)
        self.convert_btn.clicked.connect(self.convert_qt)
        self.setFixedSize(1000, 700)

    def choose_file(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Файл (*.wav);;')[0]
        self.f_path = (str(fname))

    def convert_qt(self):
        res = convert(self.f_path)
        self.res_space.setPlainText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


def convert(file_path):
    with sr.AudioFile(file_path) as source:
        audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language="ru_RU"))
            print('working on...')
            return text
        except:
            return 'Sorry.. run again..'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QPushButton, QGridLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)
        
        self.clipboard = QApplication.clipboard()                               # 1
        self.clipboard.dataChanged.connect(lambda: print('Data Changed'))    

        self.copy_btn = QPushButton('Copy', self)                               # 2
        self.copy_btn.clicked.connect(self.copy_func)               

        self.paste_btn = QPushButton('Paste', self)                             # 3
        self.paste_btn.clicked.connect(self.paste_func)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.text_edit, 0, 0, 1, 1)
        self.g_layout.addWidget(self.text_browser, 0, 1, 1, 1)
        self.g_layout.addWidget(self.copy_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.paste_btn, 1, 1, 1, 1)
        self.setLayout(self.g_layout)

    def copy_func(self):
        self.clipboard.setText(self.text_edit.toPlainText())

    def paste_func(self):
        self.text_browser.setText(self.clipboard.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
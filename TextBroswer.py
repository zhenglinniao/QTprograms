import sys
from PyQt5.QtWidgets import *

class TextBrowser(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(600, 400)

        self.write_label = QLabel("Write Text")
        self.read_label = QLabel("Read Text")
        self.write_text = QTextEdit()
        self.read_text = QTextBrowser()

      
        self.QGridLayout = QGridLayout()
        
        self.QGridLayout.addWidget(self.write_label, 0, 0)
        self.QGridLayout.addWidget(self.read_label, 0, 1)
        self.QGridLayout.addWidget(self.write_text, 1, 0)
        self.QGridLayout.addWidget(self.read_text, 1, 1)

        self.setLayout(self.QGridLayout)

        self.writetoread()
    def writetoread(self):
        self.write_text.textChanged.connect(self.show_text)
    def show_text(self):
        self.read_text.setText(self.write_text.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TextBrowser()
    ex.show()
    sys.exit(app.exec_())
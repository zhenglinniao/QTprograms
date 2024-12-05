import sys
from PyQt5.QtCore import pyqtSignal                             # 1
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    my_signal = pyqtSignal()
    def __init__(self):
        super(Demo, self).__init__()
        self.lable = QLabel('Hello World', self)
        self.lable.move(50, 50)
        self.my_signal.connect(self.my_slot)

    def my_slot(self):
        if self.lable.text() == 'Hello World':
            self.lable.setText('Hello PyQt5')
        else:
            self.lable.setText('Hello World')
       
    
    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
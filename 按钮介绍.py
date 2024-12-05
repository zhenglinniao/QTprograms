import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QPushButton('Test', self)
        self.test_button.setCheckable(True)  #设计为标记状态                       # 1
        self.test_button.setIcon(QIcon('button.svg'))               # 2
        self.test_button.toggled.connect(self.button_state_func)    # 3 按钮标记状态发生变化就会发出toggled信号

    def button_state_func(self):
        print(self.test_button.isChecked())                         # 4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
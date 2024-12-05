import sys
from PyQt5.QtWidgets import *


class FormLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("表单布局(QFormLayout)示例")
        self.resize(300, 200)

        formLayout = QFormLayout()
        formLayout.addRow(QLabel("姓名"), QLineEdit())
        formLayout.addRow(QLabel("性别"), QLineEdit())
        formLayout.addRow("性别", QComboBox())
        formLayout.addRow("出生日期", QDateEdit())
        formLayout.addRow("所在城市", QComboBox())
        formLayout.addRow("联系电话", QLineEdit())

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formLayoutDemo = FormLayoutDemo()
    formLayoutDemo.show()
    sys.exit(app.exec_())

   
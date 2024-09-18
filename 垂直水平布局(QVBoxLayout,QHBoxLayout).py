import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        print("登录主键")
        self.resize(300, 200)
        self.login_in_button = QLabel("用户名")
        self.singn_in_button = QLabel("密码")
        self.use_label = QLineEdit()
        self.pass_label = QLineEdit()
        self.use_line = QPushButton("login")
        self.pass_line = QPushButton("resign")

        self.pass_label.setEchoMode(QLineEdit.Password)#密码输入框 隐藏结果
        self.pass_label.setPlaceholderText("请输入密码")#浅色 提示字符
        self.pass_label.textChanged.connect(self.text_changed)#检测到输入框文字出现 触发槽
        self.use_label.setPlaceholderText("请输入用户名")#浅色 提示字符
        self.use_label.textChanged.connect(self.text_changed)#检测到输入框文字出现 触发槽

        self.H_box1 = QHBoxLayout()
        self.H_box1.addWidget(self.login_in_button)
        self.H_box1.addWidget(self.use_label)

        self.H_box2 = QHBoxLayout()
        self.H_box2.addWidget(self.singn_in_button)
        self.H_box2.addWidget(self.pass_label)

        self.H_box3 = QHBoxLayout()
        self.H_box3.addWidget(self.use_line)
        self.H_box3.addWidget(self.pass_line)

        self.V_box = QVBoxLayout()
        self.V_box.addLayout(self.H_box1)
        self.V_box.addLayout(self.H_box2)
        self.V_box.addLayout(self.H_box3)

        self.setLayout(self.V_box)
    def text_changed(self):
        if self.use_label.text()  and self.pass_label.text() :
            self.use_line.setEnabled(True)
        else:
            self.use_line.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
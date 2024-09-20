from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        # 创建主窗口的中心窗口
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 创建 QFrame
        self.frame = QFrame(self.central_widget)
        self.frame.setFrameShape(QFrame.Box)  # 设置为盒子形状
        self.frame.setFrameShadow(QFrame.Sunken)  # 设置为凹下的阴影效果
        self.frame.setGeometry(50, 50, 400, 300)  # 设置位置和大小

        # 创建按钮并添加到 QFrame 中
        layout = QVBoxLayout(self.frame)
        button = QPushButton('Click Me', self.frame)
        layout.addWidget(button)

        # 应用布局到 QFrame
        self.frame.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    demo = Demo()
    demo.show()
    app.exec_()

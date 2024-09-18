import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class LightSwitch(QWidget):
    def __init__(self):
        super().__init__()
        
        self.light_label = QLabel('Light is off')
        self.off_button = QRadioButton('Off')
        self.on_button = QRadioButton('On')
        self.button_group = QHBoxLayout()
        self.pic_label = QHBoxLayout()
        self.all_group = QVBoxLayout()
        self.layout_init()
        self.switch_light()
        self.pic_init()
    def layout_init(self):
        self.button_group.addWidget(self.off_button)
        self.button_group.addWidget(self.on_button)

        self.pic_label.addStretch(1)#占位符
        self.pic_label.addWidget(self.light_label)
        self.pic_label.addStretch(1)

        self.all_group.addLayout(self.button_group)
        self.all_group.addLayout(self.pic_label)

        self.setLayout(self.all_group)
    def switch_light(self):
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.pic_func)
    def pic_func(self):
        if self.off_button.isChecked():
            self.light_label.setPixmap(QPixmap('lightbulb-fill.svg'))
        else:
            self.light_label.setPixmap(QPixmap('lightbulb-off-fill.svg')) # type: ignore
    def pic_init(self):
        self.light_label.setPixmap(QPixmap('lightbulb-fill.svg'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    light_switch = LightSwitch()
    light_switch.show()
    sys.exit(app.exec_())
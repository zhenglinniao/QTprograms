#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2024/04/26
@author: Irony
@site: https://pyqt.site | https://github.com/PyQt5
@email: 892768447@qq.com
@file: TestWigglyWidget.py
@description:
"""

import sys

from PySide2.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
from WigglyWidget import WigglyWidget


class TestWigglyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TestWigglyWidget, self).__init__(*args, **kwargs)
        self._layout = QVBoxLayout(self)
        self._lineEdit = QLineEdit(self)
        self._wigglyWidget = WigglyWidget(self)
        self._layout.addWidget(self._lineEdit)
        self._layout.addWidget(self._wigglyWidget)

        self._lineEdit.textChanged.connect(self._wigglyWidget.setText)
        self._lineEdit.setText("pyqt.site")


if __name__ == "__main__":
    import cgitb
    import sys

    cgitb.enable(format="text")
    app = QApplication(sys.argv)
    w = TestWigglyWidget()
    w.show()
    sys.exit(app.exec_())

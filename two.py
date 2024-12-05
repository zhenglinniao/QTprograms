import sys
import random
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(1000, 1000)

       
        pg.setConfigOptions(leftButtonPan=False)  # 设置鼠标左键拖动平移
        pg.setConfigOption('background', 'w')  # 设置背景颜色为白色
        pg.setConfigOption('foreground', 'k')  # 设置前景颜色为黑色

        # 2
       
        # x = np.arange(100)  # 生成100个x轴数据
        # y = np.random.normal(size=100)  # 生成100个y轴数据，服从正态分布

        # r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])  # 随机选择一个符号
        # r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])  # 随机选择一个颜色

       
        self.pw1= pg.PlotWidget(title="绘制多条线")  # 创建一个绘制多条线的PlotWidget
        #self.plot_data = self.pw.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)  # 绘制多条线
        self.pw2 = pg.PlotWidget(title="绘制条状图")  # 创建一个绘制条状图的PlotWidget
        self.pw3 = pg.PlotWidget(title="绘制网格线")  # 创建一个绘制网格线的PlotWidget
        # 4
        self.plot_btn = QPushButton('Replot', self)
        self.plot_btn.clicked.connect(self.plot_slot)
        self.plot_btn.clicked.connect(self.draw1)
        self.plot_btn.clicked.connect(self.draw2)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pw1)
        self.v_layout.addWidget(self.pw2)
        self.v_layout.addWidget(self.pw3)
        self.v_layout.addWidget(self.plot_btn)
        self.setLayout(self.v_layout)

    def plot_slot(self):
        x = np.arange(100)
        y = np.random.normal(size=100)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
        self.pw1.plot(x, y, pen=pg.mkPen(color="r",width=5),symbol=r_symbol, symbolBrush=r_color) #如果不设后面参数则显示点的形状为正常点
        self.pw1.plot(x, y+2, pen=(0,0,255),symbol=r_symbol, symbolBrush=r_color)
    def draw1(self):
        x=np.arange(10)
        y1=x+1
        y2=1.1*np.cos(x+0.33)
        b1=pg.BarGraphItem(x=x,height=y1,width=0.3,brush="r")
        b2=pg.BarGraphItem(x=x,height=y2,width=0.3,brush="g")
        self.pw2.addItem(b1)
        self.pw2.addItem(b2)
    def draw2(self):
        x=np.cos(np.linspace(0,2*np.pi,1000))
        y=np.sin(np.linspace(0,4*np.pi,1000))
        self.pw3.plot(x,y,pen=pg.mkPen(color="d",width=2))
        self.pw3.showGrid(x=True,y=True) #显示网格

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
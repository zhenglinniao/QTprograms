import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView


class Demo(QTableView):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('zln')
        self.db.setUserName('root')
        self.db.setPassword('20020318')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def add_data(self):
        self.query = QSqlQuery()
        self.query.exec_('insert into students (id, class, name, score) values(3222, "0104", "zha22222222222ngsan", 90)')
        
        self.query.exec_("INSERT INTO students (id, class, name, score) VALUES (4222, '0104', '11111111111111111111', 59.5)")

        self.query.exec_("INSERT INTO students (id, class, name, score) VALUES (5222, '0104', '22222222222222222222', 59.5)")
       
        self.query.exec_("SELECT name, class, score FROM students")                # 4
        while self.query.next():
            stu_name = self.query.value(0)
            stu_class = self.query.value(1)
            stu_score = self.query.value(2)
            print(stu_name, stu_class, stu_score)

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        model = QSqlTableModel()                            # 1
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # model.setHeaderData(0, Qt.Horizontal, 'ID')
        # model.setHeaderData(1, Qt.Horizontal, 'Class')
        # model.setHeaderData(2, Qt.Horizontal, 'Name')
        # model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        #插入数据
        model.insertRow(0) #第一行插入
        model.setData(model.index(0, 0), 3222)
        model.setData(model.index(0, 1), '0104')
        model.setData(model.index(0, 2), 'zhangsan')
        model.setData(model.index(0, 3), 90)    

        model.submitAll()

        self.setModel(model)

        for i in range(model.rowCount()):               # 3
            id = model.record(i).value('id')
            name = model.record(i).value(2)
            print(id, name)

        print('---------------------')

        for i in range(model.rowCount()):               # 4
            id = model.data(model.index(i, 0))
            name = model.data(model.index(i, 1))
            print(id, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


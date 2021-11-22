import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.update()

    def update(self):
        db = sqlite3.connect('coffee.sqlite')
        cur = db.cursor()
        items = cur.execute("""SELECT id, sort, roasting, is_ground,
          description, price, volume
          FROM Coffee""").fetchall()
        db.close()
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(len(items[0]))
        self.tableWidget.setRowCount(len(items))
        for i, row in enumerate(items):
            for j, obj in enumerate(row):
                cell = obj
                if j == 3:
                    if obj == 0:
                        cell = 'В зёрнах'
                    else:
                        cell = 'Молотый'
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(cell)))
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

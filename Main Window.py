from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)

        #
        self.menu = QMenuBar()

        #
        self.database_toolbar = QToolBar()
        self.database_menu = self.menu.addMenu("Database")

        #adds actions to the menu
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        #add actions to the tool bar
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        #adds tool bar to the window
        self.addToolBar(self.database_toolbar)

        #adds menubar to the window
        self.setMenuBar(self.menu)

        #Connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)

    def close_connection(self):
        print("Database closed")
        
        
if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    aplication.exec_()

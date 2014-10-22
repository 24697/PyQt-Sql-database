from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SQLConnection import *
from DisplayWidget import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.find_data = QAction("Search Database",self)

        #creates the menu bar
        self.menu = QMenuBar()

        #
        self.database_toolbar = QToolBar()
        self.database_menu = self.menu.addMenu("Database")
        self.search_menu = self.menu.addMenu("Search")

        #adds actions to the menu
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)
        self.search_menu.addAction(self.find_data)
        
        #add actions to the tool bar
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)
        self.database_toolbar.addAction(self.find_data)

        #adds tool bar to the window
        self.addToolBar(self.database_toolbar)

        #adds menubar to the window
        self.setMenuBar(self.menu)

        #Connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)
        self.find_data.triggered.connect(self.display_products)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print(ok)

    def close_connection(self):
        pass

    def search_database(self):
        print('hold')

    def display_products(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_products_by_number((1,))
        
        
if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    aplication.exec_()

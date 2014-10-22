from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.modle = None
        self.setLayout(self.stacked_layout)
        
    def display_results_layout(self):
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_layout = addWidget(self.results_table)
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)
        self.stacked_layout.addWidget(self.results_widget)

    def show_results(self):
        if not self.model or not isinstance(self.model,"QsqlQueryNodel"):
            self.model = QsqlQueryModel()
        #set model query
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()
            
    def show_table(self):
        pass

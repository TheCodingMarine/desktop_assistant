from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.parent = parent
        
        # Create tab 1
        self.tab1 = QWidget()
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout)
        self.addTab(self.tab1, "Tab 1")
        
        #Create tab 2
        self.tab2 = QWidget()
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)
        self.addTab(self.tab2, "Tab 2")
         
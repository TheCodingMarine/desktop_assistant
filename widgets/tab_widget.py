from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from tabs.tab_1 import Tab1
from tabs.tab_2 import Tab2

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.parent = parent
        
        # Create tab 1
        self.tab1 = Tab1(self)
        self.addTab(self.tab1, "Tab 1")
        
        #Create tab 2
        self.tab2 = Tab2(self)
        self.addTab(self.tab2, "Tab 2")
         
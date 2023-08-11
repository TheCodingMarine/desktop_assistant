"""Main window of application."""
from PySide6.QtWidgets import QMainWindow, QTextEdit
from widgets.menu_bar import MenuBar
from widgets.tab_widget import TabWidget

#Create main window
class MainWindow(QMainWindow):
    """Main window of application."""
    def __init__(self, parent=None):
        """Initialize main window."""
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Desktop Assistant")
        # self.resize(1200, 800)
        self.resize(800, 600)
        
        # Show menu bar on main window
        menu = MenuBar(self)
        self.setMenuBar(menu)
        
        
        # Show tab widget on main window
        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)
        
      
        # layout = QVBoxLayout(self)
        # layout.addWidget(tab_widget)
        
    def editor(self):
        """Create editor."""
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
      
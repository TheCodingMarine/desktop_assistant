"""Main window of application."""
from PySide6.QtWidgets import QMainWindow, QTextEdit
from widgets.menu_bar import MenuBar

#Create main window
class MainWindow(QMainWindow):
    """Main window of application."""
    def __init__(self, parent=None):
        """Initialize main window."""
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Desktop Assistant")
        self.resize(1200, 800)
        
        # Show menu bar on main window
        menu = MenuBar(self)
        self.setMenuBar(menu)
        
        
    def editor(self):
        """Create editor."""
        self.textEdit = QTextEdit()
        
        
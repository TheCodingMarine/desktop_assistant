"""Main window of application."""
# Import libraries to create main window
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTextEdit
from PySide6.QtCore import QSaveFile

#Create main window
class MainWindow(QMainWindow):
    """Main window of application."""
    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.setWindowTitle("Budget App")
        self.resize(800, 600)
        
        #Create a menu bar
        self.menu_bar = self.menuBar()
        #Create a menu
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.view_menu = self.menu_bar.addMenu("View")
        self.tools_menu = self.menu_bar.addMenu("Tools")
        self.help_menu = self.menu_bar.addMenu("Help")
        
        #add actions to file menu
        #create an action
        self.open_action = self.file_menu.addAction("Open")
        self.file_dialog = QFileDialog()
        #Select file to open
        self.open_action.triggered.connect(self.file_dialog.exec)
        #open_action opens file system
        self.save_action = self.file_menu.addAction("Save")
        self.save_action.triggered.connect(self.save_file)

    def save_file(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        text = self.textEdit.toPlainText()
        file = open(name[0], 'w')
        file.write(text)
        file.close()
    
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        

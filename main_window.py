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
        self.resize(1200, 800)
        
        self.textEdit = QTextEdit()
        
        #Create a menu bar
        self.menu_bar = self.menuBar()
        
        #Create menu dropdowns
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        # self.view_menu = self.menu_bar.addMenu("View")
        self.tools_menu = self.menu_bar.addMenu("Tools")
        self.help_menu = self.menu_bar.addMenu("Help")
        
        #add open action to file menu
        self.open_action = self.file_menu.addAction("Open")
        self.file_dialog = QFileDialog()
        self.open_action.triggered.connect(self.read_file)
        
        #add save action to file menu
        self.save_action = self.file_menu.addAction("Save")
        self.save_action.triggered.connect(self.save_file_as)
        
        # Add save as action to file menu
        self.save_as_action = self.file_menu.addAction("Save As")
        self.save_as_action.triggered.connect(self.save_file_as)
        
        # Add a separator to the file menu
        self.file_menu.addSeparator()
        
        #add exit action to file menu
        self.exit_action = self.file_menu.addAction("Exit")
        self.exit_action.triggered.connect(self.close)
        
        #add undo action to edit menu
        self.undo_action = self.edit_menu.addAction("Undo")
        self.undo_action.triggered.connect(self.textEdit.undo)
    
        #add redo action to edit menu
        self.redo_action = self.edit_menu.addAction("Redo")
        self.redo_action.triggered.connect(self.textEdit.redo)
        
        #Add a separator to the edit menu
        self.edit_menu.addSeparator()

        
        #add cut action to edit menu
        self.cut_action = self.edit_menu.addAction("Cut")
        self.cut_action.triggered.connect(self.textEdit.cut)
        
        #add copy action to edit menu
        self.copy_action = self.edit_menu.addAction("Copy")
        self.copy_action.triggered.connect(self.textEdit.copy)
        
        #add paste action to edit menu
        self.paste_action = self.edit_menu.addAction("Paste")
        self.paste_action.triggered.connect(self.textEdit.paste)
        
        #add select all action to edit menu
        self.select_all_action = self.edit_menu.addAction("Select All")
        self.select_all_action.triggered.connect(self.textEdit.selectAll)
        
        # Add a separator to the edit menu
        self.edit_menu.addSeparator()
        
        #add find action to edit menu
        self.find_action = self.edit_menu.addAction("Find")
        self.find_action.triggered.connect(self.textEdit.find) 
        

    def save_file_as(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        text = self.textEdit.toPlainText()
        try:
            file = open(name[0], 'w')
        except:
            return
        file.write(text)
        file.close()
    
    def editor(self):
        self.setCentralWidget(self.textEdit)
        
    def read_file(self):
        name = QFileDialog.getOpenFileName(self, "Open File")
        if name[0]:
            file = open(name[0], 'r')
            with file:
                text = file.read()
                self.textEdit.setText(text) 
        

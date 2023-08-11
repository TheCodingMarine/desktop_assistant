from PySide6.QtWidgets import QMenuBar, QMenu, QFileDialog, QTextEdit
from windows.config_window import ConfigWindow
 
class MenuBar(QMenuBar):
    """Menu bar for main window."""
    def __init__(self, parent):
        """Initialize menu bar."""
        super(MenuBar, self).__init__(parent)
        self.parent = parent
        
        #Create a file menu  
        self.file_menu = QMenu('File', self)
        self.addMenu(self.file_menu)

        # Add open action to file menu
        self.open_action = self.file_menu.addAction("Open")
        self.open_action.triggered.connect(self.read_file)

        # Add save action to file menu
        self.save_action = self.file_menu.addAction("Save")
        self.save_action.triggered.connect(self.save_file_as)

        # Add save as action to file menu
        save_as_action = self.file_menu.addAction("Save As")
        save_as_action.triggered.connect(self.save_file_as)

        # Add a separator to the file menu
        self.file_menu.addSeparator()

        # Add exit action to file menu
        self.exit_action = self.file_menu.addAction("Exit")
        self.exit_action.triggered.connect(self.parent.close)
        
        # Create an edit menu
        self.edit_menu = QMenu('Edit', self)
        self.addMenu(self.edit_menu)
        self.textEdit = QTextEdit()

        # Add undo action to edit menu
        self.undo_action = self.edit_menu.addAction("Undo")
        self.undo_action.triggered.connect(self.textEdit.undo)

        # Add redo action to edit menu
        self.redo_action = self.edit_menu.addAction("Redo")
        self.redo_action.triggered.connect(self.textEdit.redo)
        
        # Add a separator to the edit menu
        self.edit_menu.addSeparator()
        
        # Add cut action to edit menu
        self.cut_action = self.edit_menu.addAction("Cut")
        self.cut_action.triggered.connect(self.textEdit.cut)
        
        # Add copy action to edit menu
        self.copy_action = self.edit_menu.addAction("Copy")
        self.copy_action.triggered.connect(self.textEdit.copy)
        
        # Add paste action to edit menu
        self.paste_action = self.edit_menu.addAction("Paste")
        self.paste_action.triggered.connect(self.textEdit.paste)
        
        # Add select all action to edit menu
        self.select_all_action = self.edit_menu.addAction("Select All")
        self.select_all_action.triggered.connect(self.textEdit.selectAll)
        
        # Add a separator to the edit menu
        self.edit_menu.addSeparator()
        
        # Add find action to edit menu
        self.find_action = self.edit_menu.addAction("Find")
        self.find_action.triggered.connect(self.textEdit.find)

        # Create a settings menu
        self.settings_menu = QMenu('Settings', self)
        self.addMenu(self.settings_menu)

        # Add a config action to settings menu
        self.config_action = self.settings_menu.addAction("Config")
        self.config_action.triggered.connect(self.config)
        
       

    def save_file_as(self):
        """Function for writing data to file."""
        self.file_dialog = QFileDialog()
        name = QFileDialog.getSaveFileName(self, 'Save File')
        text = self.textEdit.toPlainText()
        try:
            file = open(name[0], 'w')
        except:
            return
        file.write(text)
        file.close()
        
    def read_file(self):
        """Function for reading data from file."""
        name = QFileDialog.getOpenFileName(self, 'Open File')
        if name[0]:
            file = open(name[0], 'r')
            with file:
                text = file.read()
                self.textEdit.setText(text) 
    
    def config(self):
        """Function for opening user config settings in new window"""
        self.config_window = ConfigWindow(self)
        self.config_window.show()
        #TODO: Create config window
        #TODO: Read user config file stored as json
        #TODO: Create user config file if it doesn't exist
        #TODO: Display user config settings in config window or 
        #      default settings if no user config file exists
        #TODO: Allow user to edit config settings
        #TODO: Save user config settings to json file

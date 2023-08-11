""" Module for creating a user configuration window for the application. User
   configuration window allows the user to input settings for the 
   application."""

from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout,
                                 QGroupBox, QLabel, QLineEdit, QVBoxLayout)
import json

class ConfigWindow(QDialog):
    """User configuration window for the application."""
    def __init__(self, parent=None):
        """Initialize user configuration window."""
        super(ConfigWindow, self).__init__(parent)
        self.setWindowTitle("Configuration")
        self.resize(400, 200)
        
        # Create a layout for the configuration window
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        # Create a form layout for the configuration window
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        
        # Create a group box for the configuration window
        self.group_box = QGroupBox("User Configuration")
        self.layout.addWidget(self.group_box)
        
        # Create a label for the user name
        self.user_name_label = QLabel("User Name:")
        self.form_layout.addRow(self.user_name_label)
        
        # Create a line edit for the user name
        self.user_name_line_edit = QLineEdit()
        self.form_layout.addRow(self.user_name_line_edit)
        
        # Create a label for the user email
        self.user_email_label = QLabel("User Email:")
        self.form_layout.addRow(self.user_email_label)
        
        # Create a line edit for the user email
        self.user_email_line_edit = QLineEdit()
        self.form_layout.addRow(self.user_email_line_edit)
        
        # Create a label for the user password
        self.user_password_label = QLabel("User Password:")
        self.form_layout.addRow(self.user_password_label)
        
        # Create a line edit for the user password
        self.user_password_line_edit = QLineEdit()
        self.form_layout.addRow(self.user_password_line_edit)
        
        # Create a button box for the configuration window
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | 
                                           QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        
        # Connect the button box to the accept and reject slots
        self.button_box.accepted.connect(self.export_user_config)
        self.button_box.accepted.connect(self.close)
        self.button_box.rejected.connect(self.reject)
        self.button_box.rejected.connect(self.close)
        
        # Set focus to the user name line edit
        self.user_name_line_edit.setFocus()
        
    def get_user_name(self):
        """Return the user name."""
        return self.user_name_line_edit.text()
    
    def get_user_email(self):
        """Return the user email."""
        return self.user_email_line_edit.text()
    
    def get_user_password(self):
        """Return the user password."""
        return self.user_password_line_edit.text()
    
    # Export the user name, email, and password to json
    def export_user_config(self):
        """Export the user name, email, and password to json."""
        user_name = self.get_user_name()
        user_email = self.get_user_email()
        user_password = self.get_user_password()
        
        user_config = {"user_name": user_name, 
                       "user_email": user_email,
                       "user_password": user_password}
        
        with open("temp\\user_config.json", "w") as file:
            json.dump(user_config, file)

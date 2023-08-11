from PySide6.QtWidgets import (QFormLayout, QGroupBox, 
                               QLabel, QLineEdit, QVBoxLayout, QWidget)
class GroupBox(QWidget):
    def __init__(self):
        super(GroupBox, self).__init__()
        
        #Create a layout
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Create the group box
        self.group_box = QGroupBox("User Configuration")
        self.layout.addWidget(self.group_box)

        # Create a form layout for the group box
        self.form_layout = QFormLayout()
        self.group_box.setLayout(self.form_layout)

        # Create a user name label and line edit
        self.user_name_label = QLabel("User Name:")
        self.user_name_line_edit = QLineEdit() 
        self.user_name_line_edit.setFixedWidth(200)
        self.form_layout.addRow(self.user_name_label, self.user_name_line_edit)  
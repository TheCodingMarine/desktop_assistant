from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Tab1(QWidget):
    def __init__(self, parent=None):
        super(Tab1, self).__init__(parent)
        self.parent = parent
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
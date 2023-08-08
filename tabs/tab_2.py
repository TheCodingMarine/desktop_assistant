from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Tab2(QWidget):
    def __init__(self, parent=None):
        super(Tab2, self).__init__(parent)
        self.parent = parent

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
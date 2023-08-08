"""PySide 6 application to process inputs and formulate a budget."""
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from main_window import MainWindow

def main():
    """Main function for the application."""
    # Create an instance of QApplication
    app = QApplication([])

    # Create an instance of the main window
    window = MainWindow()
    
    # Create editor on main window
    # window.editor()
        
    # Show the main window 
    window.show()

    # Execute the application
    app.exec()
    
if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow  # Replace with your main window file and class

if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the main window and display it
    main_window = MainWindow()
    main_window.show()

    # Execute the application loop
    sys.exit(app.exec_())

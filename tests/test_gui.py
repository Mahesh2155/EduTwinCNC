import unittest
from gui.main_window import MainWindow

class TestGUI(unittest.TestCase):
    def test_main_window_creation(self):
        window = MainWindow()
        self.assertIsNotNone(window)

if __name__ == "__main__":
    unittest.main()

# test_cnc_communication.py
import unittest
from cnc_communication.cnc_connection import CNCConnection

class TestCNCConnection(unittest.TestCase):
    def test_serial_connection(self):
        conn = CNCConnection(port="COM3")
        self.assertIsNotNone(conn)

if __name__ == "__main__":
    unittest.main()

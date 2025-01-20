# test_gcode.py
import unittest
from gcode_generation.gcode_writer import write_gcode

class TestGcodeWriter(unittest.TestCase):
    def test_write_gcode(self):
        toolpaths = [{'start': (0, 0), 'end': (10, 10)}]
        gcode = write_gcode(toolpaths, "output/test.gcode")
        self.assertTrue("G1" in gcode)

if __name__ == "__main__":
    unittest.main()

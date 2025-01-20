# test_toolpath.py
import unittest
from toolpath_generation import 2d_toolpath

class TestToolpathGeneration(unittest.TestCase):
    def test_generate_2d_toolpath(self):
        cad_lines = [{'start': (0, 0), 'end': (10, 10)}]
        toolpaths = 2d_toolpath.generate_2d_toolpath(cad_lines)
        self.assertEqual(len(toolpaths), 1)

if __name__ == "__main__":
    unittest.main()

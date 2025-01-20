# 2d_toolpath.py
import numpy as np

def generate_2d_toolpath(cad_lines):
    toolpaths = []
    for line in cad_lines:
        start, end = line['start'], line['end']
        toolpaths.append({
            'start': start,
            'end': end,
            'path_type': 'linear'
        })
    return toolpaths

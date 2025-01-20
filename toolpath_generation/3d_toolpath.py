# 3d_toolpath.py
def generate_3d_toolpath(cad_lines):
    toolpaths = []
    for line in cad_lines:
        start, end = line['start'], line['end']
        toolpaths.append({
            'start': start,
            'end': end,
            'path_type': '3d_surface'
        })
    return toolpaths

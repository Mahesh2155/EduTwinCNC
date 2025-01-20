# contour_toolpath.py
def generate_contour(cad_lines):
    """Generates a contour-following toolpath."""
    toolpaths = []
    for line in cad_lines:
        toolpaths.append({
            'start': line['start'],
            'end': line['end'],
            'path_type': 'contour'
        })
    return toolpaths

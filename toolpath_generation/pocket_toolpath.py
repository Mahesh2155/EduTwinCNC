# pocket_toolpath.py
def generate_pocket(area_bounds, step_over):
    """Generates a pocket toolpath within a given area."""
    x_min, x_max, y_min, y_max = area_bounds
    toolpaths = []
    y = y_min
    while y < y_max:
        toolpaths.append({
            'start': (x_min, y),
            'end': (x_max, y),
            'path_type': 'linear'
        })
        y += step_over
    return toolpaths

# gcode_utils.py
def format_gcode_line(x=None, y=None, z=None, feed=None):
    """Format a G-code line with optional parameters."""
    line = "G1"
    if x is not None:
        line += f" X{x:.3f}"
    if y is not None:
        line += f" Y{y:.3f}"
    if z is not None:
        line += f" Z{z:.3f}"
    if feed is not None:
        line += f" F{feed:.1f}"
    return line

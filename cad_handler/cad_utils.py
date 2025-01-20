# cad_utils.py
def scale_coordinates(coords, scale_factor):
    """Scales a list of coordinates by a scale factor."""
    return [(x * scale_factor, y * scale_factor) for x, y in coords]

def translate_coordinates(coords, offset):
    """Translates coordinates by an offset."""
    return [(x + offset[0], y + offset[1]) for x, y in coords]

def validate_dxf(file_path):
    """Checks if the provided file is a valid DXF file."""
    return file_path.endswith(".dxf")

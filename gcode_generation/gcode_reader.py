# gcode_reader.py
def read_gcode(file_path):
    """Reads and parses G-code from a file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

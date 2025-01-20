# gcode_writer.py
def write_gcode(toolpaths, file_path):
    with open(file_path, 'w') as f:
        f.write("G21 ; Set units to millimeters\n")
        for path in toolpaths:
            f.write(f"G1 X{path['start'][0]} Y{path['start'][1]}\n")
            f.write(f"G1 X{path['end'][0]} Y{path['end'][1]}\n")
        f.write("M30 ; End of program\n")

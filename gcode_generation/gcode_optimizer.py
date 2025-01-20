# gcode_optimizer.py
def optimize_gcode(gcode):
    """Optimize G-code by removing redundant movements."""
    optimized_gcode = []
    last_position = None
    for command in gcode:
        if command.startswith("G1") and last_position != command:
            optimized_gcode.append(command)
            last_position = command
    return optimized_gcode

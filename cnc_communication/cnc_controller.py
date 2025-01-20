# cnc_controller.py
class CNCController:
    def __init__(self, connection):
        self.connection = connection

    def start_operation(self, gcode):
        """Send G-code to start CNC operation."""
        print("Starting CNC operation...")
        self.connection.send_gcode(gcode)

    def stop_operation(self):
        """Stop CNC operation."""
        self.connection.send_gcode(["M0 ; Stop operation\n"])
        print("CNC operation stopped.")

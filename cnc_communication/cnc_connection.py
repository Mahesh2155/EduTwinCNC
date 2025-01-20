# cnc_connection.py
import serial

class CNCConnection:
    def __init__(self, port='COM3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def send_gcode(self, gcode):
        if self.ser.is_open:
            for line in gcode:
                self.ser.write(line.encode())
        else:
            print("CNC connection is not open.")

    def close(self):
        self.ser.close()

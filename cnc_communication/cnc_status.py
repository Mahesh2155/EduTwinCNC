# cnc_status.py
def query_status(connection):
    """Queries the CNC machine for its status."""
    if connection.ser.is_open:
        connection.ser.write("STATUS\n".encode())
        return connection.ser.readline().decode().strip()
    return "Connection is closed."
def get_cnc_status(connection):
    if connection.ser.is_open:
        return "Connected"
    return "Disconnected"

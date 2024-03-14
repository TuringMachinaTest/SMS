import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    result = {}
    for port in ports:
        result[port.name] = port.device

    return result

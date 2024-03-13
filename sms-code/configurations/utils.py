import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    result = {}
    result['/dev/pts/2'] = 'dev/pts/2'
    for port in ports:
        result[port.name] = port.device

    print(result)
    return result

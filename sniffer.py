"""
Find services in a given range of ports
"""

import socket


def find_services(protocol='tcp', port_low=25, port_high=81):
    if port_low < 0 or port_high > 65535:
        print('port number out of range')
    for port in range(port_low, port_high):
        try:
            name = socket.getservbyport(port, protocol)
            print(f'{name} runs on port {port}')
        except OSError:
            pass


if __name__ == "__main__":
    find_services()

#!/usr/bin/env python3 
import socket 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "192.168.1.177"
    port = 8888

    while True:
        _input = input()
        s.sendto(str.encode(_input), (ip, port))

if __name__ == '__main__':
    main()
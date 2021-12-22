#!/usr/bin/env python3 
import socket 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "192.168.1.177"
    port = 8888

    while True:
        print("Type something and Enter")
        _input = input()
        s.sendto(str.encode(_input), (ip, port))
        resp = s.recv(1024)
        print(resp)

if __name__ == '__main__':
    main()
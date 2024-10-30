import socket
import sys

def socket_create(): #create socket to client
    try:
        global host
        global port
        global s
        host = ''
        port = 1234
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Soclet creation error: " + str(socket.error))

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error:
        print('Socket binding error: ' + str(socket.error))
        socket_bind()

def accepts():
    print("Connecting...")
    send_commands()

def send_commands():
    global s
    conn , addr = s.accept()
    print("---- Connect successful! ----\nAddress : ", addr)
    while True:
        cmd = input() + "\n"
        if cmd[:4] == "quit":
            conn.close()
            s.close()
            sys.exit()
        if cmd[:3] == 'get':
            try:
                _get = cmd[:-1].split()
                conn.send(str.encode(f"get {_get[1]}"))
                _data = conn.recv(2048)
                # data = str(_data, "utf-8")
                # if data == '': 
                #     print("This file is not exist!")
                # else:
                file = open(f"{_get[1]}", "wb")
                file.write(_data)
                file.close()
            except:
                print("Error!\n")
                continue
        elif len(str.encode(cmd)) > 0:
            try:
                conn.send(str.encode(cmd))
                client_response = conn.recv(20000)
                _client_response = str(client_response, "utf-8")
                print(_client_response, end=' ')
            except:
                typ = client_response.split(b"\n")
                for i in typ:
                    print(i)
                continue

socket_create()
socket_bind()
accepts()
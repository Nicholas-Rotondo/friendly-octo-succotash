import threading
import time
import random
import socket

print("hello")

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

def get_connection():
    server_binding = ('', 50008)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    csockid.send(msg.encode('utf-8'))

    file_name = "PROJ2-DNSTS2.txt"
    # write elements in data into file_name with each element in a seperate line
    with open(file_name, 'w') as f:
        flag = True
        while flag:
            line = csockid.recv(50008)
            if(line == ""): 
                flag = False
                break
            f.write(line.decode('utf-8') + '\n')


get_connection()
ss.close()
exit()

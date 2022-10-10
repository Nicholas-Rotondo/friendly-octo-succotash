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

def receive_from_client(csockid):
    raw_dat = csockid.recv(220)
    cleaned = raw_dat.decode('utf-8')
    return cleaned

def send_to_client(csockid, msg):
    csockid.send(msg.encode('utf-8'))

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

    file_name = "PROJ2-DNSTS2.txt"
    # write elements in data into file_name with each element in a seperate line
    new_data = receive_from_client(csockid)
    with open(file_name, 'r') as f:
        for line in f:
            if(line.split(" ")[0] == new_data):
                send_to_client(csockid, line)


get_connection()
ss.close()
exit()

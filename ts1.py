import threading
import time
import random
import socket, select

print("hello")

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

# def receive_message(csockid):
#     raw_dat = csockid.recv(220)
#     cleaned = raw_dat.decode('utf-8')

def receive_from_client(csockid):
    can_read, can_write, exceps = select.select([csockid], [], [], 10)
    data = 'nothing read'
    if(len(can_read) == 0):
        print("can_read is empty")
        return False
    
    for i in can_read:
        data = i.recv(220)
    print("Received from client, {}".format(data))
    return data

def send_to_client(csockid, msg):
    csockid.send(msg.encode('utf-8'))

def get_connection():
    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    file_name = "PROJ2-DNSTS1.txt"

    domain = receive_from_client(csockid)

    while(domain):
        ret_data(csockid, domain, file_name)
        print("domain is, {}".format(domain))
        domain = receive_from_client(csockid)

def ret_data(csockid, dns, file_name):
    with open(file_name, 'r') as f:
        for line in f:
            if(line.split(" ")[0] == dns):
                send_to_client(csockid, line)

get_connection()
ss.close()
exit()

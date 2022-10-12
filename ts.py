import threading
import time
import random
import socket, select

class Ts:
    def __init__(self, port):
        try:
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()
        server_binding = ('', port)
        ss.bind(server_binding)
        ss.listen(1)
        
        self.ls, addr = ss.accept()
       
    def receive_from_client(self):

        raw_dat = self.ls.recv(220)
        cleaned = raw_dat.decode('utf-8')
        return cleaned

    def send_to_client(self, msg):
        self.ls.send(msg.encode('utf-8'))

    def run(self):
        

        file_name = "PROJ2-DNSTS1.txt"

        

        while(self.ls.fileno() != -1):
            domain = self.receive_from_client()
            print("domain from client: {}".format(domain))
            self.ret_data(domain, file_name)
            
        

    def ret_data(self, dns, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                if(line.split(" ")[0] == dns):
                    print("sending {} to client".format(line))
                    self.send_to_client(line)

    def close_connections(self):
        self.ls.close()


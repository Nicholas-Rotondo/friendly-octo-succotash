from socket import socket, select

class Server:
    def __init__(self):
        try:
            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        cli.bind('', 50006)
        
        
        
        cli.listen(1)
        self.client, addr = cli.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))

        
        localhost_addr = socket.gethostbyname(socket.gethostname())

        ts1_port = 50007
        self.ts1.connect(localhost_addr, ts1_port)
        print("connected to ts1 at {}:{}".format(localhost_addr, ts1_port))

        ts2_port = 50008
        self.ts2.connect(localhost_addr, ts2_port)
        print("connected to ts1 at {}:{}".format(localhost_addr, ts2_port))
        
        
    def run_server(self):
        rec = self.receive_from_client()
        self.dns_request(rec)
        resp = self.get_ts_response()
        self.send_to_client(resp)


    def send_to_client(self, msg):
        self.client.send(msg.encode('utf-8'))

        
    def receive_from_client(self):
        raw_dat = self.client.recv(220)
        cleaned = raw_dat.decode('utf-8')
        return cleaned


    def dns_request(self, name):
        self.ts1.send(name.encode('utf-8'))
        self.ts2.send(name.encode('utf-8'))

    def get_ts_response(self):
        can_read, can_write, exceps = select.select([self.ts1, self.ts2], [], [], 10)
        data = 'nothing read'
        if(len(can_read) == 0):
            print("NO ONE RESPONDED !!!! (farts and dies)")
            exit()
        for i in can_read:
            data = i.recv(220)
        return data


    def close_all_connections(self):
        self.client.close()
        self.ts1.close()
        self.ts2.close()


  

if __name__ == "__main__":
    server = Server()
    server.run_server()
    server.close_all_connections()
    
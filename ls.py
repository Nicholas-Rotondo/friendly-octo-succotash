import time
import socket, select

class Server:
    def __init__(self):
        try:
            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        cli.bind(('', 50006))
        
        
        
        cli.listen(1)
        self.client, addr = cli.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))

        
        localhost_addr = socket.gethostbyname(socket.gethostname())

        ts1_port = 50007
        self.ts1.connect((localhost_addr, ts1_port))
        print("connected to ts1 at {}:{}".format(localhost_addr, ts1_port))

        ts2_port = 50008
        self.ts2.connect((localhost_addr, ts2_port))
        print("connected to ts1 at {}:{}".format(localhost_addr, ts2_port))
        
        
    def run_server(self):
        gotten = ''
        rec = self.receive_from_client()
        while(rec != None and len(rec) > 0):
            gotten = gotten + rec
            rec = self.receive_from_client()
        
        
        self.dns_request(gotten)

        broken_up = rec.split("\n")
        curr = 0
        gotten = ''
        resp = self.get_ts_response(broken_up[curr])
        while(resp != None and len(resp) > 0):
            gotten = gotten + resp
            curr = curr + 1
            resp = self.get_ts_response(broken_up[curr])

        self.send_to_client(gotten)


    def get_and_send(self):
        dns_name = self.receive_from_client()
        while(dns_name):
            self.dns_request(dns_name)
            response = self.get_ts_response(dns_name)
            self.send_to_client(response)
            dns_name = self.receive_from_client()

    def send_to_client(self, msg):
        self.client.send(msg.encode('utf-8'))

        
    def receive_from_client(self):
        #raw_dat = self.client.recv(220)
        #cleaned = raw_dat.decode('utf-8')
        #return cleaned
        can_read, can_write, exceps = select.select([self.client], [], [], 10)
        data = 'nothing read'
        if(len(can_read) == 0):
            time.sleep(3)
            if(len(can_read) == 0):
                #nothinghere.com - TIMED OUT
                return False
                
        for i in can_read:
            data = i.recv(220)
        return data


    def dns_request(self, name):
        self.ts1.send(name.encode('utf-8'))
        self.ts2.send(name.encode('utf-8'))

    def get_ts_response(self, cli_data):
        can_read, can_write, exceps = select.select([self.ts1, self.ts2], [], [], 10)
        data = 'nothing read'
        if(len(can_read) == 0):
            time.sleep(3)
            if(len(can_read) == 0):
                #nothinghere.com - TIMED OUT
                return cli_data + " - TIMED OUT"
                
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
    
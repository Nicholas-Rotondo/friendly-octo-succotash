import time
import socket, select
import sys

class Server:
    def __init__(self, ls_listen_port, ts1_hostname, ts1_listen_port, ts2_hostname, ts2_listen_port):
        try:
            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        cli.bind(('', ls_listen_port))
        
        
        
        cli.listen(1)
        self.client, addr = cli.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))

        
        

        ts1_port = ts1_listen_port
        self.ts1.connect((ts1_hostname, ts1_port))
        print("connected to ts1 at {}:{}".format(ts1_hostname, ts1_port))

        ts2_port = ts2_listen_port
        self.ts2.connect((ts2_hostname, ts2_port))
        print("connected to ts1 at {}:{}".format(ts2_hostname, ts2_port))
        
        
       


    def run_server(self):
        
        dns_name = self.receive_from_client().strip()
        while(dns_name):

            print("dns from client: {}".format(dns_name))
            self.dns_request(dns_name)
            time.sleep(0.5)
            response = self.get_ts_response(dns_name)
            print("dns from a ts: {}".format(response))
            if(not response):
            
                response = "{} - TIMED OUT".format(dns_name)
                #print("changed response to {}".format(response))
            response = response.replace('\n', ' ').replace('\r', '')
            print("the next line is what I am sending")
            print(response)
            self.send_to_client(response)
            dns_name = self.receive_from_client().strip()
        

    def send_to_client(self, msg):
        self.client.send(msg.encode('utf-8'))

        
    def receive_from_client(self):
        raw_dat = self.client.recv(220)
        cleaned = raw_dat.decode('utf-8')
        return cleaned
        


    def dns_request(self, name):
        self.ts1.send(name.encode('utf-8'))
        self.ts2.send(name.encode('utf-8'))

    def get_ts_response(self, cli_data):
        can_read, can_write, exceps = select.select([self.ts1, self.ts2], [], [], 1)
        data = 'nothing read'
        if(len(can_read) == 0):
            return False
                
        for i in can_read:
            data = i.recv(220)
        return data


    def close_all_connections(self):
        self.client.close()
        self.ts1.close()
        self.ts2.close()


  

if __name__ == "__main__":
    server = Server(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))
    server.run_server()
    server.close_all_connections()
    
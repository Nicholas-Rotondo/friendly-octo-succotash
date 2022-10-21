import sys
import socket
import sys

class Ts:
    def __init__(self, port, filename):
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
        self.filename = filename
       
    def receive_from_client(self):

        raw_dat = self.ls.recv(220)
        cleaned = raw_dat.decode('utf-8').strip()
        return cleaned

    def send_to_client(self, msg):
        self.ls.send(msg.encode('utf-8'))

    def run(self):
        

        domain = self.receive_from_client().replace('\n', ' ').replace('\r', '')
        while(domain):
            print("domain from client: {}".format(domain))
            self.ret_data(domain)
            domain = self.receive_from_client()
            
        

    def ret_data(self, dns):
        with open(self.filename, 'r') as f:
            for line in f:
                
                compare = line.strip().split(" ")[0]
                print("checking :{}:, dns is :{}:".format(compare, dns))
                print(compare == dns)
                print("because compare is {}".format(compare))
                print("one is {} long and the other is {}".format(len(compare), len(dns)))
                if(compare == dns):
                    print("sending {} to client".format(line))
                    self.send_to_client(line)

    def close_connections(self):
        self.ls.close()
if __name__ == "__main__":
    ts2 = Ts(int(sys.argv[1]), 'PROJ2-DNSTS2.txt')
    ts2.run()
    ts2.close_connections()
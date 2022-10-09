import socket

def send_message(sock, msg):
    sock.send(msg.encode('utf-8'))

def receive_message(sock):
    raw_dat = sock.recv(100)
    #cleaned = str(raw_dat, 'utf-8')
    cleaned = raw_dat.decode('utf-8')
    return cleaned

def send_from_file(cs, f):
    fi = open(f, 'r')
    for line in fi:
        send_message(cs, line)
    fi.close()


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    print(type(cs))
    # Receive data from the server
    data_from_server=cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    #send from file
    

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    client()

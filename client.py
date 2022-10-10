import socket

def send_message(sock, msg):
    sock.send(msg.encode('utf-8'))

def receive_message(sock):
    raw_dat = sock.recv(100)
    #cleaned = str(raw_dat, 'utf-8')
    cleaned = raw_dat.decode('utf-8')
    return cleaned

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50006
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)


    #send from file
    fi = open('PROJ2-HNS.txt', 'r')
    for line in fi:
        send_message(cs, line)
    fi.close()



    rec = receive_message(cs)
    while(len(rec) > 0):
        gotten = gotten + rec
        rec = receive_message(cs)

    
    fi = open('RESOLVED.txt', 'w')
    for line in gotten.split('\n'):
        if(len(line) > 0):
            print >> fi, line.strip('\n')
    fi.close()

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    client()

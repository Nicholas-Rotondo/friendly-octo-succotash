import socket

def send_message(sock, msg):
    sock.send(msg.encode('utf-8'))

def receive_message(sock):
    raw_dat = sock.recv(220)
    #cleaned = str(raw_dat, 'utf-8')
    cleaned = raw_dat.decode('utf-8')
    return cleaned

#def rec_until_done(cs):
#    gotten = ""
#    rec = receive_message(cs)
#    while(rec != None and len(rec) > 0):
#        gotten = gotten + rec
#        rec = receive_message(cs)
#    return rec

def append_resp(gotten):
    fi = open('RESOLVED.txt', 'a')
    fi.write(gotten)
    fi.close()

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


    lines = []
    fi = open('PROJ2-HNS.txt', 'r')
    for line in fi:
        lines.append(line)
    fi.close()
    
    ans = []
    for i in lines:
        if(len(i.strip()) == 0):
            break
        send_message(cs, i)
        response = receive_message(cs)
        ans.append(response)
    

    fi = open('RESOLVED.txt', 'w')
    for i in ans:
        fi.write(i)
    fi.close()


    

    
    

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    client()

import errno
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 50008))
sock.setblocking(0)

data = 'ls.py' * 1024 * 1024
data_size = len(data)
print 'Bytes to send: ', len(data)
total_sent = 0

while len(data):
    try:
        sent = sock.send(data)
        total_send += sent
        data = data[sent:]
        print 'Sending data'
    except socket.error, e:
        if e.errno != e.EAGAIN:
            raise e
        print 'Blocking with', len(data), "remaining"
        select.selct([], [sock], [])
    assert total_sent == data_size

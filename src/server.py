import socket
import threading
import sys

ip_addr = "0.0.0.0"
tcp_port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port))
server.listen(5)

def handle_client_connection(client_socket,address): 
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                client_socket.close()
            else:
                msg=request.decode()
                values = msg.split('|')
                print('Received {}'.format(values))
                msg=("OK").encode()
                client_socket.send(f"\ncpu : {values[0]}%\nmem : {values[1]}%".encode())
    except (socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))
        sys.exit(0)

print('Listening on {}:{}'.format(ip_addr, tcp_port))


while True:
    client_sock, address = server.accept()
    client_handler = threading.Thread(target=handle_client_connection,args=(client_sock,address),daemon=True)
    client_handler.start()
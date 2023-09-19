import socket

host = input ('host: ')
port = int(input ('port: '))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
print (f'\n[server] running on {host}:{port}\n')


while True:
    client_sock , client_addr = server.accept()
    print("[client] connection from : " , client_addr)


    client_sock.send("""HTTP/1.1 200 OK
Content-Type: text/html

<html><body>Hello World :)</body></html>
""".encode());


    client_sock.close()

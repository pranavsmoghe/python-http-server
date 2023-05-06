import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
request_data = client_socket.recv(1024)
response_data = b"Hi!\n"
client_socket.sendall(response_data)
client_socket.close()
server_socket.close()

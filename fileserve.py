import socket


def file_transfer_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 44468))
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on port 44468...")
    # Accept a connection from a client
    connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    # Receive the file name
    filename = connection.recv(1024).decode()
    print(f"Receiving file: {filename}")
    with open(f"received_{filename}", 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break  # No more data
            file.write(data)

    print(f"File received and saved as received_{filename}")
    connection.close()


if __name__ == '__main__':
    file_transfer_server()


OUTPUT:
Server listening on port 44468...
Connected by ('127.0.0.1', 53938)
Receiving file: cn.py
File received and saved as received_cn.py

Process finished with exit code 0

import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive messages from the server and print them
        message = client_socket.recv(1024).decode()
        print(message)

def chat_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(('localhost', 55546))
    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        # Get user input and send it to the server
        message = input()
        client_socket.sendall(message.encode())

if __name__ == '__main__':
    chat_client()

OUTPUT:
cn lab
hello world
hello scsvmv

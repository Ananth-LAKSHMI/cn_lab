import socket

def broadcast_message(message, broadcast_ip="255.255.255.255", port=9999):
    # Create a socket for broadcasting
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send the message to the broadcast address
    sock.sendto(message.encode(), (broadcast_ip, port))
    print(f"Broadcasting message to {broadcast_ip}:{port}")

# Example usage
message = "Hello, this is a broadcast message!"
broadcast_message(message)

OUTPUT:

Broadcasting message to 255.255.255.255:9999

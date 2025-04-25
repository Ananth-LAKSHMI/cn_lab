import socket
import struct

def multicast_message(message, multicast_ip="224.0.0.1", port=9999):
    # Create a socket for multicasting
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Allow reuse of address (for multicast)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Set the time-to-live (TTL) for multicast packets (e.g., 255 for the whole internet)
    ttl = struct.pack('B', 255)  # Use 'B' instead of 'b' for values 0-255
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    # Send the message to the multicast group address
    sock.sendto(message.encode(), (multicast_ip, port))
    print(f"Multicasting message to {multicast_ip}:{port}")

# Example usage
message = "Hello, this is a multicast message!"
multicast_message(message)

OUTPUT:

Multicasting message to 224.0.0.1:9999

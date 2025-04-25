import socket, uuid

# Get local IP address using a UDP socket trick
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # Google's DNS - no actual connection made
ip = s.getsockname()[0]
s.close()

# Get MAC address
mac = ':'.join(format((uuid.getnode() >> i) & 0xff, '02x') for i in range(40, -1, -8)).upper()

print("IP:", ip)
print("MAC:", mac)



OUTPUT:
IP: 172.28.0.12
MAC: 02:42:AC:1C:00:0C

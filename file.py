import socket


ALLOW_RULES = [
    ('192.168.1.100', 80),  # Allow traffic from this IP on port 80 (HTTP)
    ('192.168.1.101', 22),  # Allow traffic from this IP on port 22 (SSH)
]

BLOCK_RULES = [
    ('192.168.1.105', 80),  # Block traffic from this IP on port 80
    ('192.168.1.106', 443),  # Block traffic from this IP on port 443
]

def check_firewall(ip, port):
    # Check if the connection is allowed based on the rules
    if (ip, port) in ALLOW_RULES:
        print(f"Allowed: {ip}:{port}")
        return True
    elif (ip, port) in BLOCK_RULES:
        print(f"Blocked: {ip}:{port}")
        return False
    else:
        print(f"Unknown: {ip}:{port}, action taken: Blocked by default.")
        return False


def simulate_connection(ip, port):
    if check_firewall(ip, port):
        print(f"Connection allowed from {ip} on port {port}.")
    else:
        print(f"Connection blocked from {ip} on port {port}.")


simulate_connection('192.168.1.100', 80)  # Allowed
simulate_connection('192.168.1.106', 443)  # Blocked
simulate_connection('192.168.1.200', 25)  # Default blocked


OUTPUT:

Allowed: 192.168.1.100:80
Connection allowed from 192.168.1.100 on port 80.
Blocked: 192.168.1.106:443
Connection blocked from 192.168.1.106 on port 443.
Unknown: 192.168.1.200:25, action taken: Blocked by default.
Connection blocked from 192.168.1.200 on port 25.

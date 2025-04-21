import socket
import ssl

def download_https_web_page(hostname, path):
    port = 443
    context = ssl.create_default_context()

    # Create and wrap the socket
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            # Prepare an HTTPS GET request
            request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
            ssock.send(request.encode())

            response = b""
            while True:
                data = ssock.recv(4096)
                if not data:
                    break
                response += data

            return response.decode(errors='replace')

# Example usage for HTTPS
hostname = "www.google.com"
path = "/"

response = download_https_web_page(hostname, path)
print(response)

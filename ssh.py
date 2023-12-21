import paramiko
import socket
import threading
import sys

# You need to generate these keys (e.g., using ssh-keygen)
host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'user') and (password == 'password'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

# Create the SSH server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 22))
server.listen(100)

print("Listening for connection...")
client, addr = server.accept()

try:
    transport = paramiko.Transport(client)
    transport.add_server_key(host_key)
    server = Server()
    try:
        transport.start_server(server=server)
    except paramiko.SSHException:
        print("SSH negotiation failed.")

    channel = transport.accept(20)
    if channel is None:
        print("No channel.")
        sys.exit(1)

    print("Authenticated!")

    channel.close()

except Exception as e:
    print(f"Caught exception: {str(e)}")
    try:
        transport.close()
    except:
        pass
    sys.exit(1)

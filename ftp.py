from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Add a user with full permissions (change 'username' and 'password' to desired values)
    authorizer.add_user("username", "password", "./sharedfiles", perm="elradfmw")

    # Instantiate FTP handler and link it to the authorizer
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a port for your FTP server (21 is the default FTP port)
    port = 21

    # Instantiate and start the FTP server
    server = FTPServer(("0.0.0.0", port), handler)
    print(f"FTP server running on port {port}")
    server.serve_forever()

if __name__ == "__main__":
    main()
import socket
import time
import pickle
import ftplib
import io

# Prevent IDE error message (trivial)
result = ''

# FTP server details
ftp_server_address = 'localhost'
remote_file_path = 'remote_filename.pkl'

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers within range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
        time.sleep(0.01)  # Adding a sleep interval to slow down the loop
    return primes

def send_var_to_ftp(variable, ftp_server, remote_path, ftp_username='anonymous', ftp_password='user@example.com'):
    """
    Save a variable to an in-memory file and send it to an FTP server using anonymous login.

    :param variable: The variable to be saved and sent.
    :param ftp_server: FTP server address.
    :param remote_path: Remote path where the file will be saved on the server.
    :param ftp_username: FTP username, defaults to 'anonymous'.
    :param ftp_password: FTP password, defaults to 'user@example.com'.
    """
    # Serialize the variable to an in-memory file
    in_memory_file = io.BytesIO()
    pickle.dump(variable, in_memory_file)
    in_memory_file.seek(0)  # Rewind the file to the beginning

    # Send the in-memory file to the FTP server
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        # Use STOR command to upload the file
        ftp.storbinary('STOR ' + remote_path, in_memory_file)

def retrieve_vars_from_ftp(ftp_server, remote_path, ftp_username='anonymous', ftp_password='user@example.com'):
    """
    Retrieve a file from an FTP server, load the variables, and print them.

    :param ftp_server: FTP server address.
    :param remote_path: Remote path of the file to be retrieved.
    :param ftp_username: FTP username, defaults to 'anonymous'.
    :param ftp_password: FTP password, defaults to 'user@example.com'.
    """
    # Connect to the FTP server
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        
        # Retrieve the file into an in-memory file
        in_memory_file = io.BytesIO()
        ftp.retrbinary('RETR ' + remote_path, in_memory_file.write)
        in_memory_file.seek(0)  # Rewind the file to the beginning

        # Load the variables from the in-memory file
        variables = pickle.load(in_memory_file)
        return variables

def connect_to_server(host='localhost', port=12345):
    """Establish a connection to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def main():
    client_socket = connect_to_server()

    try:
        # Receiving range from the server
        data = client_socket.recv(1024).decode()
        start_range, end_range = map(int, data.split('-'))

        # Perform computation
        result = old_result + find_primes_in_range(start_range, end_range)
        print(f"Primes in range {start_range}-{end_range}:\n")

        my_data = {'result': result}

        # Save the variable and send it to FTP using anonymous login
        send_var_to_ftp(my_data, ftp_server_address, remote_file_path)

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    # Try to access FTP
    try:
        retrieved_data = retrieve_vars_from_ftp(ftp_server_address, remote_file_path)

        for key, value in retrieved_data.items():
            globals()[key] = value
        old_result = result

    # If There is no pkl file
    except:
        old_result = []
        print("Starting fresh")
    main()

# Retrieved data (test if successful)
retrieved_data = retrieve_vars_from_ftp(ftp_server_address, remote_file_path)
for key, value in retrieved_data.items():
    globals()[key] = value
print(result)
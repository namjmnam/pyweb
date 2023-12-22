import pickle
import ftplib
import io

# Prevent IDE error message (trivial)
key1 = ''
key2 = ''
key3 = ''

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

# Example usage
my_data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# FTP server details
ftp_server_address = 'localhost'
remote_file_path = 'remote_filename.pkl'

# Save the variable and send it to FTP using anonymous login
send_var_to_ftp(my_data, ftp_server_address, remote_file_path)
retrieved_data = retrieve_vars_from_ftp(ftp_server_address, remote_file_path)

for key, value in retrieved_data.items():
    globals()[key] = value

# Retrieved data
print(key1)
print(key2)
print(key3)

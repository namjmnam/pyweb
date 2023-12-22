import pickle
import ftplib
import io

def save_var(variable, filename):
    """
    Save a variable to a file.

    :param variable: The variable to be saved.
    :param filename: The name of the file where the variable will be saved.
    """
    with open(filename, 'wb') as file:
        pickle.dump(variable, file)

def load_var(filename):
    """
    Load a variable from a file.

    :param filename: The name of the file from which to load the variable.
    :return: The loaded variable.
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)

def send_file_to_ftp(ftp_server, ftp_username, ftp_password, file_path, remote_path):
    """
    Send a file to an FTP server.

    :param ftp_server: FTP server address.
    :param ftp_username: FTP username.
    :param ftp_password: FTP password.
    :param file_path: Local path to the file to be sent.
    :param remote_path: Remote path where the file will be saved on the server.
    """
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        with open(file_path, 'rb') as file:
            ftp.storbinary('STOR ' + remote_path, file)

def retrieve_and_print_file_from_ftp(ftp_server, ftp_username, ftp_password, remote_path):
    """
    Retrieve a file from an FTP server and print its contents.

    :param ftp_server: FTP server address.
    :param ftp_username: FTP username.
    :param ftp_password: FTP password.
    :param remote_path: Remote path of the file to be retrieved.
    """
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        with open('temp_file', 'wb') as file:
            ftp.retrbinary('RETR ' + remote_path, file.write)
        
        with open('temp_file', 'r') as file:
            print(file.read())

def save_var_and_send_to_ftp(variable, ftp_server, ftp_username, ftp_password, remote_path):
    """
    Save a variable to an in-memory file and send it to an FTP server.

    :param variable: The variable to be saved and sent.
    :param ftp_server: FTP server address.
    :param ftp_username: FTP username.
    :param ftp_password: FTP password.
    :param remote_path: Remote path where the file will be saved on the server.
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

# Example usage
my_data = {'key1': 'value1', 'key2': 'value2'}

# FTP server details
ftp_server_address = 'localhost'
ftp_username = ''
ftp_password = ''
remote_file_path = 'remote_filename.pkl'

# Save the variable and send it to FTP
save_var_and_send_to_ftp(my_data, ftp_server_address, ftp_username, ftp_password, remote_file_path)
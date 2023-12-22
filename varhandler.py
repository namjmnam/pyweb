import pickle
import ftplib

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

# Example usage
my_data = {'key1': 'value1', 'key2': 'value2'}
filename = 'saved_data.pkl'

# Save the variable
save_var(my_data, filename)

# Load the variable
loaded_data = load_var(filename)
print(loaded_data)


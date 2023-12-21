import ftplib
import os

def download_all_files(ftp_server, destination_folder):
    # Connect to the FTP server
    with ftplib.FTP(ftp_server) as ftp:
        # Use anonymous login
        ftp.login()

        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # List files in the root directory
        files = ftp.nlst()

        # Download each file
        for filename in files:
            local_path = os.path.join(destination_folder, filename)
            with open(local_path, 'wb') as file:
                ftp.retrbinary('RETR ' + filename, file.write)

# Replace 'your_ftp_server.com' with your FTP server's address
ftp_server_address = 'localhost'

# Local folder to save files
destination_folder = './fetched'

# Download all files
download_all_files(ftp_server_address, destination_folder)

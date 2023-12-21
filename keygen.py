import paramiko

def generate_ssh_key_pair(key_type=paramiko.RSAKey, bits=2048):
    """
    Generate an SSH key pair.
    
    Args:
    - key_type: The type of key to generate (paramiko.RSAKey or paramiko.DSSKey).
    - bits: Number of bits in the key (default: 2048).

    Returns:
    - A tuple (private_key_str, public_key_str) containing the private and public keys as strings.
    """
    key = key_type.generate(bits=bits)
    private_key_str = key.write_private_key_str()
    public_key_str = f"{key.get_name()} {key.get_base64()}"
    return private_key_str, public_key_str

private_key, public_key = generate_ssh_key_pair()
print("Private Key:\n", private_key)
print("Public Key:\n", public_key)

# Optionally, save these keys to files
with open("private_key.pem", "w") as private_file:
    private_file.write(private_key)

with open("public_key.pub", "w") as public_file:
    public_file.write(public_key)

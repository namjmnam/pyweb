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

# Save the private key to 'test_rsa.key'
with open("test_rsa.key", "w") as private_file:
    private_file.write(private_key)

# Optionally, save the public key to a file (e.g., 'test_rsa.pub')
with open("test_rsa.pub", "w") as public_file:
    public_file.write(public_key)

print("Private key saved to 'test_rsa.key'")
print("Public key saved to 'test_rsa.pub'")

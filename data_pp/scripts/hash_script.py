import pandas as pd
import hashlib

# Generate unique hash value for each sequence

# Function to generate a 6-digit hash for a given sequence
def generate_hash(sequence):
    # Create a hash object using SHA-1 algorithm
    hash_object = hashlib.sha1()
    # Update the hash object with the sequence
    hash_object.update(sequence.encode())
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    # Take the first 3 bytes of the hash and convert them to an integer
    hash_int = int(hash_hex[:6], 16)
    # Modulo the integer with 1,000,000 to ensure it fits within 6 digits
    hash_value = hash_int % 1000000
    return hash_value

# Read the CSV file
df = pd.read_csv("output.csv")

# Generate hash values for each sequence
hash_values = []
for sequence in df["SEQUENCE"]:
    hash_value = generate_hash(sequence)
    hash_values.append(hash_value)

# Add a new column "HASH" to the DataFrame with the hash values
df["HASH"] = hash_values

# Write the updated DataFrame back to the CSV file
df.to_csv("update_list.csv", index=False)


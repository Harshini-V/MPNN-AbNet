import hashlib
import csv
import random

# Generates hash values for each cluster

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

def parse_fasta(filename):
    clusters = {}
    previous_chain_id = None
    with open(filename, 'r') as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                chain_id = line.split(" ")
                chain_id = chain_id[0][1:]
                if previous_chain_id == None:
                    previous_chain_id = chain_id
                if chain_id == previous_chain_id:
                    hash_value = generate_hash(chain_id)
                    clusters[chain_id] = hash_value
                    previous_chain_id = chain_id
                elif chain_id != previous_chain_id:
                    # Chain ID already in a cluster, assign the same cluster ID
                    clusters[chain_id] = hash_value
                    previous_chain_id = chain_id

            else:
                # Skip sequences, we're only interested in headers
                pass    
    return clusters

def add_hash_column_to_csv(csv_file, clusters):
    # Read the CSV file and add a new column for hash values
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['CLUSTER']
        rows = list(reader)
    
    # Update the rows with hash values
    for row in rows:
        chain_id = row['CHAINID']
        if chain_id in clusters:
            row['CLUSTER'] = clusters[chain_id]
        else:
            # Handle the case where the chain ID is not found in the clusters dictionary
            row['CLUSTER'] = 'Not Found'
            print(row)

    # Write the updated rows to a new CSV file
    with open('output_list.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def split_hash_values(unique_hashes):
    # Calculate the size of each split
    total_hashes = len(unique_hashes)
    train_size = int(total_hashes * 0.8)
    validation_size = test_size = (total_hashes - train_size) // 2

    # Shuffle the list of unique hash values
    random.shuffle(unique_hashes)

    # Split the list into train, validation, and test sets
    train_set = unique_hashes[:train_size]
    validation_set = unique_hashes[train_size:train_size + validation_size]
    test_set = unique_hashes[train_size + validation_size:]

    return train_set, validation_set, test_set

def write_to_file(hash_values, filename):
    with open(filename, 'w') as file:
        for hash_value in hash_values:
            file.write(str(hash_value) + '\n')

# Example usage:
clusters = parse_fasta("/home/hice1/lfogel3/scratch/data_pp/mmseqs2/clusterRes_all_seqs.fasta")
add_hash_column_to_csv("/home/hice1/lfogel3/scratch/data_pp/update_list.csv", clusters)


# Example usage:
unique_hashes = list(set(clusters.values()))
train_set, validation_set, test_set = split_hash_values(unique_hashes)

write_to_file(validation_set, 'valid_clusters.txt')
write_to_file(test_set, 'test_clusters.txt')


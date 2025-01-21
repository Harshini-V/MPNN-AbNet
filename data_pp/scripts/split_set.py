import random

# Splits data into test, training, and validation sets
# Outputs test and validation data into files called 'test.txt' and 'validation.txt'

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
train_set, validation_set, test_set = split_hash_values(unique_hashes)

write_to_file(validation_set, 'validation.txt')
write_to_file(test_set, 'test.txt')

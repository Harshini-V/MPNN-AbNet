from Bio import SeqIO
import pandas as pd

# Path to the input fasta file
fasta_file = "/home/hice1/lfogel3/scratch/data_pp/out/antibody.fasta"

# List to store data
data = []

# Parse the fasta file
for record in SeqIO.parse(fasta_file, "fasta"):
    # Parse the fasta header
    header_parts = record.description.split()
    #print(header_parts)
    chain_id = header_parts[0]  # Remove ">" and convert to uppercase
    deposition = header_parts[1]
    if header_parts[3] == 'None':
        resolution = 0.0
    else:
        resolution = float(header_parts[3])
    sequence = str(record.seq)
    
    # Append data to the list
    data.append([chain_id, deposition, resolution, sequence])

# Create a DataFrame
df = pd.DataFrame(data, columns=["CHAINID", "DEPOSITION", "RESOLUTION", "SEQUENCE"])

# Write DataFrame to CSV file
df.to_csv("output.csv", index=False)

# Create Enviroment
mamba create -n mmseq2
mamba activate mmseq2
mamba install -c conda-forge -c bioconda mmseqs2

# Cluster with mmseq2
mmseqs easy-cluster antibody.fasta clusterRes tmp --min-seq-id 0.3 -c 0.8 --cov-mode 1
#!/bin/bash
#SBATCH -JProteinMPNNrun_antibodies
#SBATCH -N 1 --ntasks-per-node=10
#SBATCH --mem-per-gpu=16G
#SBATCH -t 30:00
#SBATCH --gres=gpu:V100:1
#SBATCH --mail-user=lfogel3@gatech.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH -o pMPNN_ab_run1.out

# based on the given example script submit_example_1.sh

module load anaconda3/2022.05.0.1
conda activate proteinMPNN

folder_with_pdbs="/home/hice1/lfogel3/scratch/data_pp/pdb_files"

output_dir="/home/hice1/lfogel3/scratch/data_pp/output/MPNN_abTrial"
if [ ! -d $output_dir ]
then
    mkdir -p $output_dir
fi

path_for_parsed_chains=$output_dir"/parsed_pdbs.jsonl"

python ../helper_scripts/parse_multiple_chains.py --input_path=$folder_with_pdbs --output_path=$path_for_parsed_chains

python ../protein_mpnn_run.py \
        --jsonl_path $path_for_parsed_chains \
        --out_folder $output_dir \
        --num_seq_per_target 2 \
        --sampling_temp "0.1" \
        --seed 37 \
        --batch_size 1

conda deactivate

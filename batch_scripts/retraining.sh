#!/bin/bash
#SBATCH -JMPNN-AbNetRetraining5             # Job name
#SBATCH -N 1 --ntasks-per-node=32           # Request nodes and tasks per node
#SBATCH --mem-per-gpu=64G                   # memory per gpu
#SBATCH -t 16:00:00                         # time
#SBATCH --gres=gpu:V100:1                   # request GPU
#SBATCH --mail-user=lfogel3@gatech.edu      # if you want to get emails when it starts/ends/fails put that here
#SBATCH --mail-type=BEGIN,END,FAIL          # specify start/end/fail/etc here
#SBATCH -o training_5.out 	            # output log. not the actual output

module load anaconda3/2022.05.0.1
conda activate proteinMPNN

python /home/hice1/lfogel3/scratch/ProteinMPNN/training/training.py --path_for_training_data /home/hice1/lfogel3/scratch/data_pp/training --path_for_outputs /home/hice1/lfogel3/scratch/data_pp/training/model5 --num_epochs 100
 
conda deactivate


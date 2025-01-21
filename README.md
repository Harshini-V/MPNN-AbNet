# MPNN-AbNet
Message Passing Neural Network for Antibody Sequence Design
Based on the model designed by [ProteinMPNN](https://github.com/dauparas/ProteinMPNN)

## Modifications
We made slight changes to the ProteinMPNN scripts to get it to work with our data. We still followed the same general model architecture, and oriented our data the same way for easier running.

## Retraining and Running the Model
We first retrained the model using antibody data rather than general protein data.
### Commands used
First create a conda environment 
```
conda create -n proteinMPNN
conda activate proteinMPNN
conda install python=3.10 # need at least python3.x for pMPNN
#from the github
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
conda install biopython scipy
```
Everything was run using batch scripts on Georgia Tech's PACE-ICE service. Links provided to the scripts below.
[Model Retraining]
[Running the main model]

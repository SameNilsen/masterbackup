#!/bin/bash

# Job name:
#SBATCH --job-name=simpleLLMtest
#
# Project:
#SBATCH --account=ec12
#
# Wall time limit:
#SBATCH --time=00:10:00 # for 10min
#
# Other parameters:
#SBATCH --mem-per-cpu=12G
#SBATCH --qos=devel
#SBATCH --partition=accel
#SBATCH --gpus=1 # could be a100:1 to specify gpu type.
#SBATCH --ntasks=1

## Set up job environment:
set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

pip list

# activate the virtual environment
source $HOME/masters/mastertestenv/bin/activate

# Load modules
# module --quiet purge  # Reset the modules to the system default
module load Python/3.12.3-GCCcore-13.3.0
module list

pip list

# Set the ${PS1} (needed in the source of the virtual environment for some Python versions)
#export PS1=\$

## Do some work:
python3 $HOME/masters/simple_llms/testPureLLM.py
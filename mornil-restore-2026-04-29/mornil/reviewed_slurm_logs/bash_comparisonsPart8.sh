#!/bin/bash

# Job name:
#SBATCH --job-name=compPart8
#
# Project:
#SBATCH --account=ec12
#
# Wall time limit:
#SBATCH --time=00:15:00 # for 15min
#
# Other parameters:
#SBATCH --mem-per-cpu=16G
#SBATCH --qos=devel
#SBATCH --partition=accel
#SBATCH --gpus=h100nv:1 # could be a100:1 to specify gpu type, or just 1 to get a random one.
#SBATCH --ntasks=1

## Set up job environment:
set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

nvidia-smi

echo "RUNNING: python3 /fp/projects01/ec12/mornil/comparisons/comparisonsV2/comparison2.py --model normistral11b_thinking --quantization full --model_length 32768 --gpu_usage 0.8 --inference_provider vllm --dtype half --order serial --gpu h100nv_94GB"

pip list

echo "Setting up..."

echo "Current directory:"
pwd

echo "Contents of current directory:"
ls

echo "Setting HF_HOME var:"
export HF_HOME=/fp/projects01/ec12/mornil/hf_cache
echo "HF_HOME set to $HF_HOME"
echo "Setting VLLM_CACHE_ROOT var:"
export VLLM_CACHE_ROOT=/fp/projects01/ec12/mornil/vllm_cache
echo "VLLM_CACHE_ROOT set to $VLLM_CACHE_ROOT"


# Load modules
# module --quiet purge  # Reset the modules to the system default
module load Python/3.12.3-GCCcore-13.3.0
module list

# activate the virtual environment
source /fp/projects01/ec12/mornil/mastertestenv/bin/activate

pip list

# Set the ${PS1} (needed in the source of the virtual environment for some Python versions)
#export PS1=\$

echo "Checking installed packages..."
pip list | grep -e transformers -e torch -e langchain -e nest-asyncio -e bitsandbytes -e accelerate -e tiktoken -e dotenv -e faiss-cpu -e sentence-transformers -e vllm

echo "Ready to go."

## Do some work:
echo "----------------SERIAL----------------"
python3 /fp/projects01/ec12/mornil/comparisons/comparisonsV2/comparison2.py --model normistral11b_thinking --quantization full --model_length 32768 --gpu_usage 0.8 --inference_provider vllm --dtype half --order serial --gpu h100nv_94GB
echo "----------------PARALLEL----------------"
python3 /fp/projects01/ec12/mornil/comparisons/comparisonsV2/comparison2.py --model normistral11b_thinking --quantization full --model_length 32768 --gpu_usage 0.8 --inference_provider vllm --dtype half --order parallel --gpu h100nv_94GB
echo "----------------XBRL----------------"
python3 /fp/projects01/ec12/mornil/comparisons/comparisonsV2/comparison2.py --model normistral11b_thinking --quantization full --model_length 32768 --gpu_usage 0.8 --inference_provider vllm --dtype half --order xbrl --gpu h100nv_94GB
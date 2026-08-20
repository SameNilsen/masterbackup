#!/bin/bash

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
echo "Setting TRITON_CACHE_DIR var:"
export TRITON_CACHE_DIR=/fp/projects01/ec12/mornil/triton_cache
echo "TRITON_CACHE_DIR set to $TRITON_CACHE_DIR"

echo "Loading Python module..."
module load Python/3.12.3-GCCcore-13.3.0

echo "Starting virtual environment..."
source gptossenv/bin/activate

echo "Checking installed packages..."
pip list | grep -e transformers -e torch -e triton -e kernels -e accelerate

echo "Ready to go."
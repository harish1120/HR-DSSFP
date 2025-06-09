#!/bin/bash
# We load cuda and cudnn because we want to use the GPU version of Tensorflow

module --force purge
module load StdEnv/2023 gcc/12.3 opencv/4.11.0 cuda/12.2 cudnn/8.9.5.29 scipy-stack/2024b python/3.11.5
# module load StdEnv/2023 gcc/12.3 python/3.12 cuda/12.2 cudnn/8.9.5.29 scipy-stack/2024b
# Try loading scipy-stack last (if available)
# module load scipy-stack/2025a
export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CUDA_HOME

# scipy-stack is a bundle that contains a lot of commonly-used python packages
# such as numpy, scipy, pandas, matplotlib, jupyter, etc.
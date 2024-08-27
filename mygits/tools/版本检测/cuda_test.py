import torch

if torch.cuda.is_available():
    cuda_version = torch.version.cuda
    print("CUDA 版本:", cuda_version)
else:
    print("CUDA 不可用，请检查 CUDA 是否正确安装并配置。")
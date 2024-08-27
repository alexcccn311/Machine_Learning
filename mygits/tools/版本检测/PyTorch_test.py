import torch

# 检查 PyTorch 版本
print("PyTorch 版本:", torch.__version__)

# 检查 CUDA 是否可用
cuda_available = torch.cuda.is_available()
print("是否支持 CUDA:", cuda_available)

# 如果 CUDA 可用，打印 CUDA 版本和当前设备信息
if cuda_available:
    print("CUDA 版本:", torch.version.cuda)
    print("GPU 设备数量:", torch.cuda.device_count())
    print("当前使用的 GPU 设备:", torch.cuda.get_device_name(0))
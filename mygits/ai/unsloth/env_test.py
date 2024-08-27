import torch

# 检查 PyTorch 版本
print("PyTorch 版本:", torch.__version__)

# 检查 CUDA 是否可用
cuda_available = torch.cuda.is_available()
print("CUDA 是否可用:", cuda_available)

if cuda_available:
    # 获取当前设备名称
    device_name = torch.cuda.get_device_name(0)
    print("CUDA 设备名称:", device_name)
else:
    print("未检测到 CUDA 设备")
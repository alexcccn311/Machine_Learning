from uiautomation import WindowControl

window_name = 'Final_product3'
check_window = WindowControl(SubName=window_name)

# 先确认是否找到窗口
if check_window.Exists(maxSearchSeconds=1):
    print(f"{window_name}窗口已找到")
    check_window.SetActive()  # 切换到目标窗口
else:
    print(f"{window_name}窗口未找到")
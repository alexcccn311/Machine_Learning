from uiautomation import WindowControl
import time

def send_wechat_message(text):
    # 绑定微信主窗口
    wx = WindowControl(Name='微信')

    def wx_message(message):
        wx.SendKeys(message, waitTime=0)
        wx.SendKeys('{Enter}', waitTime=0)

    # 检查微信窗口是否存在
    if wx.Exists(maxSearchSeconds=1):
        wx.SetActive()  # 切换到微信窗口
        time.sleep(0.5)  # 等待窗口切换完成
        wx_message(text)  # 发送消息

        # 绑定并切换回 PyCharm 窗口
        pycharm = WindowControl(SubName='Final_product3')  # 使用窗口部分名称匹配
        if pycharm.Exists(maxSearchSeconds=1):
            pycharm.SetActive()  # 切换回 PyCharm 窗口
        else:
            print("Final_product3窗口未找到")
        douyin = WindowControl(SubName='抖音')  # 使用窗口部分名称匹配
        if douyin.Exists(maxSearchSeconds=1):
            douyin.SetActive()  # 切换回 PyCharm 窗口
    else:
        print("微信窗口未找到")

send_wechat_message('已连接直播间弹幕')
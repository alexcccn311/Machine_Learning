from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 启动浏览器
Wd = webdriver.Chrome()

# 打开指定的URL
Wd.get(
    'https://live.douyin.com/81299375964?column_type=single&is_aweme_tied=0&search_id=202407160859348C8D012CB1DCA068501E&search_result_id=7392013788028931364')

# 等待页面加载
time.sleep(10)

# 存储已获取的弹幕内容
previous_danmaku = set()
new_danmaku = set()


def get_danmaku():
    global new_danmaku
    try:
        # 找到所有包含弹幕内容的元素
        danmaku_elements = Wd.find_elements(By.CLASS_NAME, 'webcast-chatroom___content-with-emoji-text')

        # 提取并打印新的弹幕文本
        current_danmaku = set()
        for element in danmaku_elements:
            current_danmaku.add(element.text)

        # 找到真正的新弹幕
        new_danmaku = current_danmaku - previous_danmaku
        for text in new_danmaku:
            print(text)

        # 更新已获取的弹幕内容
        previous_danmaku.update(new_danmaku)
    except Exception as e:
        print(f"Error: {e}")


# 持续抓取最新弹幕信息
try:
    while True:
        get_danmaku()
        time.sleep(2)  # 每隔2秒抓取一次弹幕内容
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    # 关闭浏览器
    Wd.quit()
    Wd.quit()
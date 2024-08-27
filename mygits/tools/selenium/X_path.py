#作者：Alex
#2024 / 8 / 25
#上午11: 51

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import html

def get_web_text(url, xpath_expression):
    options = Options()
    # 使用当前用户的数据目录，替换为你的Chrome用户数据目录路径
    options.add_argument(r"user-data-dir=D:\Chrome\chrome-win64\chrome-win64\MyChromeUserData")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载

        user_input = input("请输入 'go' 以继续执行: ")
        while user_input.strip().lower() != 'go':
            user_input = input("输入无效，请输入 'go' 以继续执行: ")

        # 定位包含所有目标文本的元素
        elements = driver.find_elements(By.XPATH, xpath_expression)

        # 初始化一个列表来保存所有段落的文本
        all_text = []

        for element in elements:
            text = element.text  # 获取文本内容
            all_text.append(text)

        # 将所有段落文本拼接成一个完整的字符串
        full_text = '\n'.join(all_text)

        return full_text
    except NoSuchElementException:
        return "未找到指定的元素"
    finally:
        driver.quit()

def save_text_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text)
        print("文件写入完成。")

if __name__ == '__main__':
    url = 'https://www.pixiv.net/novel/show.php?id=19718987#3'
    xpath_expression = '//span[@data-textcount]'
    file_path = r"D:\git\gitstorege\LLM_practice\ai\data\knowledge_base\txt\性奴训练学院\Chapter_2.txt"

    text = get_web_text(url, xpath_expression)
    save_text_to_file(file_path, text)
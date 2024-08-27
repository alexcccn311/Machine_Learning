from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import html

def get_web_text(url, class_name, tag_name):
    options = Options()
    # 使用当前用户的数据目录，替换为你的Chrome用户数据目录路径
    options.add_argument(r"user-data-dir=D:\Chrome\chrome-win64\chrome-win64\MyChromeUserData")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载

        # user_input = input("请输入 'g' 以继续执行: ")
        # while user_input.strip().lower() != 'g':
            # user_input = input("输入无效，请输入 'g' 以继续执行: ")

        # 定位包含所有目标文本的容器
        container = driver.find_element(By.CLASS_NAME, class_name)

        # 获取容器中所有的 <p> 标签
        p_elements = container.find_elements(By.TAG_NAME, tag_name)

        # 初始化一个列表来保存所有段落的文本
        all_text = []

        for p_element in p_elements:
            html_content = p_element.get_attribute('innerHTML')
            text = html.unescape(html_content)
            all_text.append(
                text.replace('<br>', '\n').replace('<br/>', '\n').replace('<p>', '\n').replace('</p>', '\n'))

        # 将所有段落文本拼接成一个完整的字符串
        full_text = '\n'.join(all_text)

        return full_text
    except NoSuchElementException:
        return "未找到指定的元素"
    finally:
        driver.quit()

def get_web_text_css_selector(url, css_selector):
    options = Options()
    # 使用当前用户的数据目录，替换为你的Chrome用户数据目录路径
    options.add_argument(r"user-data-dir=D:\Chrome\chrome-win64\chrome-win64\MyChromeUserData")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载

        # user_input = input("请输入 'g' 以继续执行: ")
        # while user_input.strip().lower() != 'g':
            # user_input = input("输入无效，请输入 'g' 以继续执行: ")

        # 使用 CSS 选择器定位包含所有目标文本的元素
        elements = driver.find_elements(By.CSS_SELECTOR, css_selector)

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
    url = 'https://www.pixiv.net/novel/show.php?id=22637981#2'
    class_name = 'sc-iemWCZ'  # 从你的截图中选择合适的 class_name
    tag_name = ''  # 如果有具体的 tag_name，设置为对应的标签名；如果没有，则留空
    file_path = r"D:\git\gitstorege\LLM_practice\ai\data\knowledge_base\txt\性奴训练学院\Chapter_61.txt"
    css_selector = 'span.text-count'

    if tag_name:  # 如果提供了具体的 tag_name，调用基于 tag_name 的函数
        text = get_web_text(url, class_name, tag_name)
    else:  # 如果未提供 tag_name，调用基于 CSS 选择器的函数
        text = get_web_text_css_selector(url, css_selector)

    save_text_to_file(file_path, text)
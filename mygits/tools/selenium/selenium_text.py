# web_text_extractor.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import html


def get_web_text(url, class_name, tag_name):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载
        container = driver.find_element(By.CLASS_NAME, class_name)
        p_element = container.find_element(By.TAG_NAME, tag_name)  # 获取该容器中的第一个<p>标签
        html_content = p_element.get_attribute('innerHTML')
        text = html.unescape(html_content)
        return text.replace('<br>', '\n').replace('<br/>', '\n').replace('<p>', '\n').replace('</p>', '\n')
    except NoSuchElementException:
        return "未找到指定的元素"
    finally:
        driver.quit()


def save_text_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text)
        print("文件写入完成。")

if __name__ == '__main__':
    get_web_text(url, class_name, tag_name)
    save_text_to_file(file_path, text)
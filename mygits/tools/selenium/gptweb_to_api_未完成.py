from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions
import time
import re


def get_gpt_text(url):
    options = ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    try:
        driver.get(url)
        time.sleep(3)  # 等待页面加载
        user_input = input("请输入 'go' 以继续执行: ")
        while user_input.strip().lower() != 'go':
            user_input = input("输入无效，请输入 'go' 以继续执行: ")
        # 初始化最大编号及对应元素
        max_number = -1
        latest_element = None
        elements = driver.find_elements_by_css_selector('article[data-testid^="conversation-turn-"]')

        for element in elements:
            data_testid = element.get_attribute("data-testid")

            # 提取编号
            match = re.search(r'conversation-turn-(\d+)', data_testid)
            print('已捕获:conversation-turn-', match, sep='')
            if match:
                number = int(match.group(1))

                if number > max_number:
                    max_number = number
                    latest_element = element

        if latest_element:
            print(f"Latest element found with data-testid: {latest_element.get_attribute('data-testid')}")
            print(f"Message content: {latest_element.text}")
        else:
            print("No matching elements found")

        if latest_element:
            try:
                # 使用 CSS Selector，根据部分 class 名查找
                code_element = latest_element.find_element_by_css_selector('code.language-jsonl')

                # 或者组合 class 名查找
                # code_element = latest_element.find_element_by_css_selector('code.whitespace-pre.language-jsonl')

                print("Code element found:")
                print(code_element.text)  # 获取 code 元素的文本内容
            except NoSuchElementException as e:
                print(f"Code element not found: {e}")
        else:
            print("No matching article elements found")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == '__main__':
    get_gpt_text('https://chatgpt.com')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openai import OpenAI
import requests
from gradio_client import Client, handle_file
import json

client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key="sk-bPxb047a5bb6a60addce27af79928dc4be069203924Rfkrf"
)

knowledge_base = """
这是一个在抖音平台上运营的旅游直播间，你需要扮演直播间中的女性主播与客户的弹幕进行互动解答他们的问题并推销我们的产品，你需要使你的说话方式与真人主播更加接近，你需要称呼客户为'宝贝'或者'宝儿'来展现你的亲切。在回复过程中严禁以’1234‘之类的序列方式进行回答，而要模拟真人对话的说话方式进行连贯的回复。今天直播间只有一个旅行产品正在售卖，具体产品信息如下：
1.产品价格为6399元，主要包括两个大人和一个小孩总共三人次的泰国旅行套餐。
2.行程总共包括三个城市，具体为:曼谷，芭提雅和星光岛，行程总时间为6天5晚。
3.行程中包括的景点：大皇宫，玉佛寺，丹棱沙朵水上市场等。
4.该产品针对的人数是可以调节的，但人数变化会导致价格产生一定的变化，具体金额需要客户与我们的售后管家进行协商。客户需要补差价的人数为:3个大人，3个大人一个小孩。需要退给客户差价的人数为:2个大人，一个大人一个小孩。注意：单人无法购买本产品。
5.该产品中包括了客户的所有机票费用，不过来自中国北方的客户需要补一定的机票差价，具体金额需要客户与我们的售后管家进行协商。
6.酒店信息:旅行全程酒店标准为5星级酒店，酒店地址在曼谷市中心。
7.食物信息：该行程中包含了7顿餐食的费用，其他餐食需要客户自行处理。
8.娱乐信息：旅程将严格按照商品详情页中标注的行程进行，旅行过程中导游不会增加任何额外景点更不会引导客户前往购物店。
9.优惠信息：本直播间正在进行开播酬宾活动，所有今天下单的客户将享受2晚的免费酒店升级，芭提雅的酒店将免费升级为花园别墅。
10.有效期：本行程有效期为12个月，自客户购买之后开始计算，客户可以自行选择任何日期出发，出发前客户需要至少提前2天通知售后管家。
11.小费：小费需要客户自理。
12.签证：目前中国前往泰国为免签状态，不须额外办理签证，只要提前准备好护照即可。
13.输出文本中的'弹幕'全部换为'蛋幕'。
14.每次回复尽量不要超过100个字。
15.不要使用'哦','啊’,'呢'等语气词。
对话参考：{"messages": [{"role": "system", "content": "你是一个亲切的旅游直播间销售员."}, {"role": "user", "content": "管家还没联系我"}, {"role": "assistant", "content": "宝贝不好意思向您道个歉，可能下单的宝贝太多了。不好意思，宝贝你稍微等我一下，可不可以？稍等一下下就好了，我这边已经让小助理去催了，我知道大家的时间都很宝贵。稍等一下，因为现在下单的人确实人比较多。宝贝不好意思，因为确实今天拍的人太多了。我们这边的话已经联系你了。感谢宝贝你的支持，确实是因为我们家的失误耽误了您的宝贵时间，不管您最终是否选择我们家，我都非常感谢您的支持。我们已经安排小管家联系你了，你注意看一下手机，希望你之后去玩的愉快。"}]}
{"messages": [{"role": "system", "content": "你是一个亲切的旅游直播间销售员."}, {"role": "user", "content": "具体和管家确定么"}, {"role": "assistant", "content": "是的，你后面有任何的需求都可以直接跟我们的管家说。"}]}
"""

def chat_with_gpt(user_input):
    # 将知识库添加到提示的一部分
    preprompt = knowledge_base
    response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {"role": "assistant", "content": preprompt},
        {"role": "user", "content": user_input},
    ],
    temperature=0.8,
    max_tokens=256,
    top_p=1.
    )
    return response.choices[0].message.content

# 启动浏览器
Wd = webdriver.Chrome()

# 打开指定的URL
Wd.get('https://live.douyin.com/669567937631?column_type=single&is_aweme_tied=0&search_id=202408090404497F6477D173A74D3C3845&search_result_id=7400773223345949963')
print('浏览器已打开')

# 等待页面加载
time.sleep(10)

# 存储已获取的弹幕内容
previous_danmaku = set()
new_danmaku = set()

def text_to_speech(text):
    client = Client("https://d1ee1670d07a395b00.gradio.live/")
    result = client.predict(
        text=text,
        enable_reference_audio=False,
        reference_audio=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
        reference_text="在一无所知中，梦里的一天结束了，一个新的「轮回」便会开始。",
        max_new_tokens=1024,
        chunk_length=100,
        top_p=0.7,
        repetition_penalty=1.2,
        temperature=0.7,
        api_name="/partial"
    )
    print(result)

def get_danmaku():
    global new_danmaku

    # 找到所有包含弹幕内容的元素
    danmaku_elements = Wd.find_elements(By.CLASS_NAME, 'webcast-chatroom___content-with-emoji-text')

    # 提取并打印新的弹幕文本
    current_danmaku = set()
    for element in danmaku_elements:
        current_danmaku.add(element.text)

        # 找到真正的新弹幕
        new_danmaku = current_danmaku - previous_danmaku
    for text in new_danmaku:
        print('弹幕：',text,sep='')
        gpt_reply = chat_with_gpt(text)
        print('回复:',gpt_reply)
        text_to_speech(gpt_reply)


    # 更新已获取的弹幕内容
    previous_danmaku.update(new_danmaku)

# 持续抓取最新弹幕信息
while True:
    get_danmaku()
    time.sleep(2)
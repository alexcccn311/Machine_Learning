import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import requests
import pyaudio
import pygame
import random
import asyncio
from wechat_Msg import send_wechat_message
from api import initialize_client
from uiautomation import WindowControl
import os
import glob

pygame.mixer.init()
danmuku_history, new_danmuku = set(), set()
selected_danmu = ''
response, stream, p, answer_audio_file, last_introduction_audio = None, None, None, None, None

with open('knowledge_base.txt', 'r', encoding='utf-8') as f:
    knowledge_base = f.read()


introduction_base_dir = r"voice/introduce"
ending_base_dir = r"voice/ending"

# 使用 glob 模块查找所有的 .wav 文件
introduction_audio_files = glob.glob(os.path.join(introduction_base_dir, "**", "*.wav"), recursive=True)
ending_audio_files = glob.glob(os.path.join(ending_base_dir, "*.wav"))

answer_map = {
    '机票': r"voice/pre_danmu/机票/机票.wav",
    '酒店': r"voice/pre_danmu/酒店/酒店.wav",
    '有没有小团': r"voice/pre_danmu/有没有小团/有没有小团.wav",
    '购物': r"voice/pre_danmu/购物/购物.wav",
    '两大一小': r"voice/pre_danmu/两大一小/两大一小.wav",
    '两个大人一': r"voice/pre_danmu/两大一小/两大一小.wav",
    '两大': r"voice/pre_danmu/两大/两大.wav",
    '两个大人': r"voice/pre_danmu/两个大人/两个大人.wav",
    '一大一小': r"voice/pre_danmu/一大一小/一大一小.wav",
    '三大一小': r"voice/pre_danmu/三大一小/三大一小.wav",
    '国庆': r"voice/pre_danmu/节假日/节假日.wav",
    '过年': r"voice/pre_danmu/节假日/节假日.wav",
    '寒假': r"voice/pre_danmu/节假日/节假日.wav",
    '元旦': r"voice/pre_danmu/节假日/节假日.wav",
    '春节': r"voice/pre_danmu/节假日/节假日.wav",
    '没有联系': r"voice/pre_danmu/没有联系/没有联系.wav"
}

replace_dict = {
    '哦': '',
    '弹幕': '蛋幕',
    '2399': '两千三百九十九',
    '护照': '护某照',
    '3999': '三千九百九十九',
    '4399': '四千三百九十九',
    '*': '',
    '藏': '葬',
    '订单后四位': '手机后四位'
}
web_location = {
    '风旅行': 'https://live.douyin.com/344078063819?column_type=single&is_aweme_tied=0&search_id=2024081717170904DF99825B60D5A7AAF5&search_result_id=7404034722965359898',
    '中国国旅西北游': 'https://live.douyin.com/890006552788?column_type=single&is_aweme_tied=0&search_id=20240818163905F149DED31380590B502F&search_result_id=7404357759015095562',
    '带你游泰国': 'https://live.douyin.com/995653781051?column_type=single&is_aweme_tied=0&search_id=202408181741598BE8B4E9926CAB571109&search_result_id=7404409432349707539',
    '仙本那小玩家': 'https://live.douyin.com/109259981373?column_type=single&is_aweme_tied=0&search_id=20240818174730F33C82CD26EEDF612D15&search_result_id=7404342376795327778',
    '丫丫带你看世界': 'https://live.douyin.com/360053599287?column_type=single&is_aweme_tied=0&search_id=20240819174044CDDE4E35EECE6C041F63&search_result_id=7404751561852833035',
    '花样北京':'https://live.douyin.com/116625528411?column_type=single&is_aweme_tied=0&search_id=202408200254091BEF5CA4CD94133F1AE0&search_result_id=7404865378297416995',
    'COCO带你游泰国':'https://live.douyin.com/481448262160?column_type=single&is_aweme_tied=0&search_id=20240820030522C11C965B528F27493D02&search_result_id=7404909471014718771'
}


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
        max_tokens=512,
        top_p=1.
    )
    return response.choices[0].message.content


def text_to_speech(text):
    # POST请求URL
    url = 'http://127.0.0.1:5000/tts'

    # 请求体
    data = {
        "character": "jiarguolv",
        "text": text,
        "text_language": "zh",
        "format": "wav",
        "stream": "true",
        "emotion": "default",
        "speed": "1.0",
        "top_k": "5",
        "top_p": "0.8",
        "temperature": "0.8",
        "save_temp": "False",
        "batch_size": "1"
    }

    # 初始化pyaudio
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=p.get_format_from_width(2),
                    channels=1,
                    rate=32000,
                    output=True)

    # 使用requests发送POST请求获取音频流
    response = requests.post(url, json=data, stream=True)

    return response, stream, p


def play_response(response, stream, p):
    # 读取数据块并播放
    for data in response.iter_content(chunk_size=1024):
        stream.write(data)

    # 停止和关闭流
    stream.stop_stream()
    stream.close()

    # 终止pyaudio
    p.terminate()


async def ending_play():
    random_ending_audio = random.choice(ending_audio_files)
    pygame.mixer.music.load(random_ending_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # 等待当前音频播放完毕
        await asyncio.sleep(0.1)


def get_danmuku():
    global new_danmuku

    # 找到所有包含弹幕内容的元素
    danmuku_elements = Wd.find_elements(By.CLASS_NAME, 'webcast-chatroom___content-with-emoji-text')

    # 提取并打印新的弹幕文本
    current_danmuku = set()
    for element in danmuku_elements:
        current_danmuku.add(element.text)
        # 找到真正的新弹幕
        new_danmuku = current_danmuku - danmuku_history


async def event_listener():
    global response, stream, p, danmuku_history, answer_audio_file, selected_danmu
    i = 1
    while True:
        get_danmuku()
        if len(new_danmuku) == 0:
            print('没有新弹幕。', i, sep='')
            await asyncio.sleep(1)
            i += 1
        else:
            selected_danmu = random.choice(list(new_danmuku))
            send_wechat_message(selected_danmu)
            print(new_danmuku)
            print('已获取新弹幕：', selected_danmu, sep='')
            danmuku_history.update([selected_danmu])
            if any(keyword in selected_danmu for keyword in
                   ['ai', '机器人', 'AI', '人工智能', 'Ai', 'aI', '可以', '好的']):
                selected_danmu = ''
                continue
            for key in answer_map:
                if key in selected_danmu:
                    answer_audio_file = answer_map[key]
                    break
            if answer_audio_file:
                while selected_danmu:
                    await asyncio.sleep(1)
                continue  # 重新开始 while True 循环
            else:
                gpt_reply = chat_with_gpt(selected_danmu)
                tts_text = selected_danmu + '?' + gpt_reply
                print('回复：', tts_text, sep='')
                for key, value in replace_dict.items():
                    tts_text = tts_text.replace(key, value)
                # 特殊处理数字 '2'
                if '2' in tts_text:
                    if '2个' in tts_text:
                        tts_text = tts_text.replace('2个', '两个')
                    if '2号' not in tts_text:
                        tts_text = tts_text.replace('2', '两')
                response, stream, p = text_to_speech(tts_text)
                while selected_danmu:
                    await asyncio.sleep(1)


async def task1():
    global last_introduction_audio
    available_audio_files = [audio for audio in introduction_audio_files if audio != last_introduction_audio]
    random_introduction_audio = random.choice(available_audio_files)
    last_introduction_audio = random_introduction_audio
    pygame.mixer.music.load(random_introduction_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # 等待当前音频播放完毕
        await asyncio.sleep(0.1)


async def task2():
    global answer_audio_file
    global selected_danmu
    if answer_audio_file:
        # noinspection PyTypeChecker
        pygame.mixer.music.load(answer_audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 等待当前音频播放完毕
            await asyncio.sleep(0.1)
        selected_danmu = ''
        answer_audio_file = None
        await (ending_play())
    else:
        # noinspection PyTypeChecker
        play_response(response, stream, p)
        selected_danmu = ''
        await (ending_play())


async def main():
    # 启动 event_listener 作为后台任务
    # noinspection PyAsyncCall
    asyncio.create_task(event_listener())

    while True:
        if len(new_danmuku) != 0:
            await task2()
        else:
            await task1()


# 主程序

with open('api_key.json', 'r', encoding='utf-8') as f:
    api_dict = json.load(f)


api_name = input(f"请输入连接的api端口：{', '.join(api_dict.keys())}：")
client = initialize_client(api_dict, api_name)


# 启动浏览器
Wd = webdriver.Chrome()
pycharm = WindowControl(SubName='Final_product3')  # 使用窗口部分名称匹配
if pycharm.Exists(maxSearchSeconds=1):
    pycharm.SetActive()  # 切换回 PyCharm 窗口
while True:
    target_url = input(f"请选择目标直播间。选项：{', '.join(web_location.keys())} 或直接输入URL：")
    # 打开指定的URL
    if target_url in web_location:
        # 使用键名对应的 URL
        Wd.get(web_location[target_url])
        print(f"已进入 {target_url} 的直播间")
        break
    elif target_url.startswith('http://') or target_url.startswith('https://'):
        # 如果输入是 URL，则直接打开
        Wd.get(target_url)
        print("已打开输入的 URL")
        break
    else:
        print("输入的键名或URL无效，请重试")

# 等待页面加载
time.sleep(3)

while True:
    try:
        asyncio.run(main())
    except Exception as e:
        # 发送错误消息
        error_message = f"出现错误: {str(e)}"
        send_wechat_message(error_message)
        print("重新启动 main()...")

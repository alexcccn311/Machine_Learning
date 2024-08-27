import random
import tkinter as tk
from tkinter import font
from threading import Thread
import time

def create_window(message, delay=None, followup_message=None):
    root = tk.Tk()
    root.title("提醒")
    root.attributes("-topmost", True)
    window_width = 350
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"+{position_x}+{position_y}")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    custom_font = font.Font(family="Helvetica", size=13, weight="bold")

    label = tk.Label(frame, text=message, padx=20, pady=5, font=custom_font)
    label.pack(pady=10)

    def on_button_click():
        root.destroy()
        if delay is not None and followup_message is not None:
            def delayed_followup():
                time.sleep(delay / 1000)  # 将毫秒转换为秒
                create_window(followup_message)
            Thread(target=delayed_followup).start()

    button = tk.Button(frame, text="贱奴遵命", command=on_button_click, padx=20, pady=10, font=custom_font)
    button.pack(pady=2)

    root.mainloop()

# 随机生成一个布尔值
random_boolean = random.choice([4, 3, 2, 1, 0])
message_2 = '好了，贱奴，你可以休息了。'

if random_boolean != 1:
    message_1 = random.choice([
        '贱奴，快趴下让我肏死你！',
        '贱奴，快爬过来舔我的鸡吧！',
        '贱奴，现在立刻练习高跟鞋走路！'
    ])
    delay = random.randint(20,60) * 60 * 1000  # 10秒
    create_window(message_1, delay, message_2)
else:
    create_window(message_2)
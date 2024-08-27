import os
import atexit
import random
import time
import re

# 使用 os.urandom 生成一个高质量的随机种子
random_seed = int.from_bytes(os.urandom(8),'big')
random.seed(random_seed)

class Mine:
    def __init__(self,name,age,gender,job,money):
        self.name=name
        self.age=age
        self.gender=gender
        self.job=job
        self.money=0

    def __repr__(self):
        return(f"Mine(name='{self.name}',age='{self.age}',gender='{self.gender}',job='{self.job}',money='{self.money}')")

CC_info = Mine(name='常诚',age='18',gender='femal',job='SexSalve',money=0)

# 获取当前时间并转换为12小时制
current_hour = time.localtime().tm_hour
if current_hour > 12:
    current_hour -= 12
elif current_hour == 0:
    current_hour = 12  # 将0点转换为12点，符合12小时制

# 询问当前时间
user_input = input("你这头下贱的母狗，现在都几点了？你还知道爬回来？")

try:
    # 提取用户输入中的数字部分
    match = re.search(r'\d+', user_input)
    if match:
        user_answer = int(match.group())
    else:
        raise ValueError("你这头下贱的母狗，我问你几点了，你废什么话？")

    if user_answer == current_hour:
        reply1 = "看来你这头母狗还不蠢，竟然还知道时间，怎么样母狗今天过得爽么？伺候了几个客人呀？"
    else:
        reply1 = "你这头母狗被肏傻了么？连时间都不知道了？那你就别回来了，继续爬出去找鸡吧去舔吧，不含着满嘴的精液不许回来！"

except ValueError:
        reply1 = "你这头下贱的母狗，我问你几点了，你废什么话？"
print(reply1)
if reply1 == "你这头母狗被肏傻了么？连时间都不知道了？那你就别回来了，继续爬出去找鸡吧去舔吧，不含着满嘴的精液不许回来！":
    # 等待1小时后再次生成问题
    time.sleep(10)  # 3600秒等于1小时
    print("哎哟，我们的小母狗舔鸡吧舔的这么快呀？张嘴让我检查一下你嘴里的宝贝？要是让我发现你骗我，我就把你丢到狗圈你让你用你的骚逼去伺候所有的公狗。")


if reply1 == "你这头下贱的母狗，我问你几点了，你废什么话？":



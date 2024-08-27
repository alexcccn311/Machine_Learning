import random
import requests:
a=1
b=100
random_number = random.randint(a,b)
print(random_number)

# 从 random.org 获取真随机数
response = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
true_random_number = int(response.text.strip())

print(true_random_number)
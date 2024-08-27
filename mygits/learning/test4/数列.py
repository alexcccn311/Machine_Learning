numbers = list(range(7, 24))  # range(7, 24) 生成从 7 到 23 的数列，包含 7，但不包含 24
print(numbers)

def is_prime(n):
    """检查一个数是否是质数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_series(start, end):
    """生成从 start 到 end 之间的质数数列"""
    prime_series = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_series.append(num)
    return prime_series

a= int(input('从几开始:'))
b= int(input('从几结束:'))
print(generate_prime_series(a,b))
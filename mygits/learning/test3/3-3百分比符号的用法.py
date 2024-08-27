def is_prime(n): #检查n是否为质数，def代表定义。这里将is_prime(n)定位为了一个具有特殊意义的临时函数，具体定义方式通过下方缩进的内容进行。
    """检查一个数是否为质数"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1): #设定i的范围为2至根号n+1范围内的所有整数，n ** 0.5就是算n的平方根，int定义了整数,range代表范围。
        if n % i == 0: #如果n除以i的余数为0则判定失败，i的值在前文进行了设定.
            return False
    return True
primes = [n for n in range(2, 100) if is_prime(n)] #n for n in range(2, 100)这一段定义了n的取值范围，if定义了判定方式。整体定义了primes是这个数列的名字。
print(primes)
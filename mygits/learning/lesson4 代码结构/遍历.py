for i in range(10):
    print(i)
for a in 'python':
    print(a)
for b in range(1,10):
    if b%2 == 0:
        print('%2是算余数')
    else:
        print(b)
d=0
for c in range(1,10):
    d+=c    #d+=c等同于d=d+c
print(d)

for e in range(100,999):
    if e == e//100 ** 3 + int((e%100)/10) ** 3+ (e%10) ** 3:          #水仙花数#  #//代表整除，**代表幂运算，%代表求余数）
        print(e)
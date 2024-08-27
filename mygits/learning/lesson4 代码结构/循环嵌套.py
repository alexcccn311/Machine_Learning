#长方形#
for i in range(1,4):
    for j in range(1,5):
        print('*',end=" ")
    print("")

for i in range(1,4):
    print()

#直角三角形#
for i in range(1,6):
    print(i*'*')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()

for i in range(1,4):
    print()

#反直角三角形#
for i in range(1,6):
    print((6-i)*'*')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end="")
    print()


for i in range(1,4):
    print()

#正三角形#
for i in range(1,6):
    print((5-i)*' ',(2*i-1)*'*',sep='')

for i in range(1,6):
    for k in range(1,6-i):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end="")
    print()

for i in range(1,4):
    print()

#菱形#
for i in range(1,8):
    if i <= 4:
        print((4-i)*' ',(2*i-1)*'*',(4-i)*' ',sep='')
    else:
        print((i-4)*' ',(15-2*i)*'*',(i-4)*' ',sep='')

for i in range(1,8):
    if i <= 4:
        for k in range(1,5-i):
            print(' ',end='')
        for j in range(1,2*i):
            print('*',end="")
    else:
        for k in range(1,i-3):
            print(' ',end='')
        for j in range(1,16-2*i):
            print('*',end='')
    print()

def diamond(num):
    while num % 2 == 0:
        num = int(input('偶数行数无法生成菱形，请重新输入:'))

    else:
        for i in range(1, num+1):
            if num%2 == 1:
                if i <= (num+1)/2:
                    for k in range(1, (num+1)//2 + 1 - i):
                        print(' ', end='')
                    for j in range(1, 2 * i):
                        print('*', end="")
                else:
                    for k in range(1, i - (num-1)//2):
                        print(' ', end='')
                    for j in range(1, 2*(num+1) - 2 * i):
                        print('*', end='')
                print()
num_request_diamond = int(input('请输入所需菱形的行数：'))

diamond(num_request_diamond)


for i in range(1,4):
    print()

#空心菱形#
def hollow_diamond(num):
    while num % 2 == 0:
        num = int(input('偶数无法生成空心菱形，请重新输入:'))
    else:
        mid_num = (num+1) // 2
        for i in range(1,num+1):
            if i <= mid_num:
                for k in range(1, mid_num - i +1):
                    print(' ', end='')
                print('*',end='')
                if i == 1:
                    print()
                elif i != 1:
                    for j in range(1, (i-1) * 2):
                        print(' ',end='')
                    print('*',end='\n')
            elif i > mid_num:
                for k in range(1, i - mid_num+1):
                    print(' ', end='')
                print('*',end='')
                if i == num:
                    print()
                    break
                if i != num:
                    for j in range(1, num -2*(i-mid_num) -1):
                        print(' ',end='')
                    print('*',end='\n')
num_request_hollow_diamond = int(input('请输入空心菱形的行数：'))
hollow_diamond(num_request_hollow_diamond)

print(10*'--')

#心形#

import math
def heart(high):
    width = int(30/13 * high)
    for i in range(-high,high):
        for j in range(-width,width):
            x = j / (width / 2)
            y = -(i / (high / 2))
            equation = (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3
            if i==0 and j==0:
                print('H',end='')
            elif equation <= 0:
                print('*',end='')
            else:
                print(' ', end='')
        print()

user_high = int(input('想要爱心的高度是：'))
heart(user_high)
###心形形状不完美(调整宽高比例解决，原因在于每个字符的宽高比例并不是1比1.在1920*1080分辨率的情况下，字符长宽比例为1.88，因此16需要乘以1.88，结果为30.08取值为30即可。不过字体导致的比例并没有确定，懒得弄了差不多就行。），心形的高度和宽度也无法正确生成（解决，高度为x=0时的高度，即x=13时高度为（-6,6）总计13个点。）###
###尚未解决，坐标系尺寸无法完美匹配心形图案。（坐标系尺寸问题解决需要确定心形最高点最低点和最宽点，x=0和y=0时并不是心形的极值，求心形的极值需要用到高数相关知识。具体技术栈为：导数>求极限>python中求极值。暂时搁置）###
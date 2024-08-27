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


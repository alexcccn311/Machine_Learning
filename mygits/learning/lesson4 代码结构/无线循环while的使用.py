def get_answer():
    return input('今天你要接客么？Y/N')
answer = get_answer()
while answer == 'Y' or answer == 'y':
    print('臭婊子，知道还不快爬去门口接客？把你的骚屁股再摇用力一点，让那些男人们能看到你有多骚')
    answer = get_answer()

lucky_num = int(input('请输入你今天的幸运数字：'))
def add_all(number):
    a=0
    b=0
    while a <= number:
        b += a
        a += 1
    return b
final_result = add_all(lucky_num)
print(final_result)

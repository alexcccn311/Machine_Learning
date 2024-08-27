a = int(input('a='))
b = int(input('b='))
print('a> b? Y/N')
is_greater = a > b
un_greater = b >= a
while True:
    user_input = input().strip().upper()
    if user_input == 'Y' or user_input == 'yes':
        if is_greater:
            print('correct')
        if un_greater:
            print('wrong')
        break
    elif user_input == 'N' or user_input == 'no':
        if is_greater:
            print('wrong')
        if un_greater:
            print('correct')
        break
    else:
        print('Invalid input, please input Y or N.')

print('a* b? ')
while True:
    user_input2 = input().strip()
    try:
        user_answer = int(user_input2)
    except ValueError:
        print('Invalid input, please enter an integer.')
        continue
    if user_answer == (a*b):
        print('correct')
        break
    else:
        print('wrong.and pls answer again.')
passwords_dict = {
    "user1": "PASSWORD1",
    "user2": "PASSWORD2",
    "user3": "PASSWORD3"
}
attempt_counts = {
    "user1": 0,
    "user2": 0,
    "user3": 0,
}

def check_password(account,password):
    if account in passwords_dict and password == passwords_dict[account]:
        return True
    else:
        attempt_counts[account] += 1
        return False

login_successful = False
while not login_successful:
    account = input('请输入您的账号：')
    password = input('请输入您的账号密码: ')
    if check_password(account,password):
        print('登陆成功')
        login_successful = True
    elif account not in passwords_dict:
        print('该账号不存在')
    elif attempt_counts[account] >= 3:
        print('您已输错3次密码，账号已冻结。')
    else:
        print('密码错误，您还有',3-attempt_counts[account],'次机会，请重新输入。', sep='')




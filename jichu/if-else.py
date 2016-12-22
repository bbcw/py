#coding:utf-8

# def account_login():
#     passwd = input('Password: ')
#     if passwd == '123456':
#         print('Login success!')
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()
passwd_list = ['*#*#','12345']
def account_login():
    passwd = input('Password: ')
    passwd_correct = passwd == passwd_list[-1]
    passwd_reset = passwd == passwd_list[0]
    if passwd_correct:
        print('Login success!')
    elif passwd_reset:
        new_passwd = input('Enter a new password: ')
        passwd_list.append(new_passwd)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid unput!')
        account_login()
account_login()
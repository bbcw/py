#coding:utf-8
passwd_list = ['*#*#','12345']
def account_login():
    n = 3
    while n > 0:
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
            n = n - 1
            print(n,'time left')
    else:
        print('Your account has been suspended')
account_login()
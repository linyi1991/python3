'''
Version: 0.1.0
Author: TheoYu
簡易測試驗證密碼，if迴圈判別
'''
account = 'root'
pwd = '123456'
acc = str(input('Please input username: '))
password = str(input('Please input password: '))
if acc == account and password == pwd:
    print('Success login!!')
else:
    print('Please try again!')
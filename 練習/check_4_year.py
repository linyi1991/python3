'''
Version: 0.1.0
Author: TheoYu
'''

year = int(input('輸入西元任意年: '))
check_y = year / 4 == 0 or year % 4 == 0 or year // 100 == 0


if check_y and True:
    print(f'西元{year}是閏年')
else:
    print(f'西元{year}不是閏年')



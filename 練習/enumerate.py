'''
Version 0.1.0
Author: TheoYu
'''

# enumerate 測試

items = ['Apple', 'Banana', 'Orange']

# for 循環取出
for index in range(len(items)):
    print(f'{index} 項目為 {items[index]}')

print()
# 採用 enumerate
for index, item in enumerate(items):
    print(f'{index} 項目為: {item}')

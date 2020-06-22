person = {'name': 'TheoYu', 'age': '30', 'weight': '70', 'hight': '171'}
# 檢查name和tel是否存在
print('name' in person, 'tel' in person)
# 使用age將person內的30修改為18
if 'age' in person:
    person['age'] = 25
# 操作索引操作插入2個person新鍵值
person['tel'] = '1238884202'
person['signature'] = '學習python'
print('name' in person, 'tel' in person)
# 檢查字典中鍵的數量
print(len(person))

# 對字典循環，並取出鍵值關係
for key in person:
    print(f'{key}: {person[key]}')

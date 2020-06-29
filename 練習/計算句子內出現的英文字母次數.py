'''
輸入一段英文字，並計算每個字母出現的次數並統計
Version: 0.1.0
Author: TheoYu
'''

sentence = input('請輸入任意英文字母: ')
dic = {}

for word in sentence:
    if 'A' <= 'wrod' <= 'Z' or 'a' <= 'word' <= 'z':
        dic[word] = dic.get(word, 0) + 1

for key, value in dic.items():
    print(f'{key}出現了{value}次')
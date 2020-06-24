'''
Version: 0.1.0
Author: TheoYu
'''
# 三個人，五個科目，放入成績欄位
names = ['Alex', 'Boa', 'Cherry']
courses = ['Chinese', 'Math', 'China', 'Franch', 'Japanese' ]
scores = [[0] * len(courses) for _ in range(len(names))]
print(scores)
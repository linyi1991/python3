'''
計算五個學生，每個學生各三門考試成績
並在令誤算每個學生平均分數，以及該門課平均分數
'''

names = ['Alex', 'Boa', 'Cherry']
courses = ['Chinese', 'Math', 'China', 'Franch', 'Japanese' ]
scores = [[0] * len(courses) for _ in range(len(names))]
# 導入分數
for i, name in enumerate(names):
    print(f'請輸入{name}的成績 >>>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}:'))
print('*' * 5, '學生平均成績', '*' * 5)

# 計算每個學生的平均分數
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均分數為: {avg_score:.1f}分')
print('*' * 5, '平均科目成績', '*' * 5)

# 計算每門課程的平均分數
for index, course in enumerate(courses):
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均分數：{avg_score:.1f}分')
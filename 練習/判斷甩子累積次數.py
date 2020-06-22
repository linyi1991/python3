import random

counters = [0] * 6
print(counters)
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}點數出现了{counters[face - 1]}次')


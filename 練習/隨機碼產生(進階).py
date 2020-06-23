import random
import string

ALL_Chars = string.ascii_letters + string.digits

def generate_code(len_code=4):
    '''定義預設產生長度4個字元'''
    return ''.join(random.choices(ALL_Chars, k=len_code))

print(generate_code())


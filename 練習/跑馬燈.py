import os
import time
context = 'Hello ! Are you look me?'
while True:
    os.system('clear')
    print(context)
    time.sleep(0.5)
    context = context[1:] + context[0]
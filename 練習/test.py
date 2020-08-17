'''
Version: 0.1.0
Author: TheoYu
'''

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n = int(num)
        if n > largest:
            largest = n
        elif smallest is None:
            smallest = n
        elif n < smallest:
            smallest = n
    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)


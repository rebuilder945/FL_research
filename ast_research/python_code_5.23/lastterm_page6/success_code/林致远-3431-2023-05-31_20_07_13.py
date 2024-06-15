num = eval(input())
def ju(x):
    if x % 2 == 0:
        return True
    else:
        return False
if num < 0 or num > 36:
    print('error')
elif num == 0:
    print('green')
elif num <= 10:
    if ju(num):
        print('black')
    else:
        print('red')
elif num <= 18:
    if ju(num):
        print('red')
    else:
        print('black')
elif num <= 28:
    if ju(num):
        print('black')
    else:
        print('red')
else:
    if ju(num):
        print('red')
    else:
        print('black')

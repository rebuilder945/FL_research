a = input()
b = input()
if a == b:
    print('error')
else:
    if a == 'red' and b == 'blue' or b == 'red' and a == 'blue':
        print('purple')
    elif a == 'red' and b == 'yellow' or b == 'red' and a == 'yellow':
        print('orange')
    elif a == 'blue' and b == 'yellow' or b == 'blue' and a == 'yellow':
        print('green')

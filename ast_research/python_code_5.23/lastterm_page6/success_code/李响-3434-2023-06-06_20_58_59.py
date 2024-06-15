a = eval(input())
b = eval(input())
if (a == b) or (a or b) == 'red'or'blue'or'yellow':
    print('error')
else:
    if (a or b) == 'blue' or 'red':
        print('purple')
    elif (a or b) =="blue" or 'yellow':
        print('green')
    elif (a or b) == 'red' or 'yellow':
        print('orange')

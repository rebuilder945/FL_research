yuan1 = eval(input())
yuan2 = eval(input())
if yuan1 == 'red' and yuan2 == 'purple':
    print('purple')
if yuan2 == 'red' and yuan1 == 'purple':
    print('purple')
if yuan1 == 'red' and yuan2 == 'yellow':
    print('orange')
if yuan2 == 'red' and yuan1 == 'yellow':
    print('orange')
if yuan1 == 'blue' and yuan2 == 'yellow':
    print('green')
if yuan2 == 'blue' and yuan1 == 'yellow':
    print('green')
else:
    print('error')

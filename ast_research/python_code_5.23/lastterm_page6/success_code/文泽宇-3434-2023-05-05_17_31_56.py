yuan1 = str(input())
yuan2 = str(input())
if yuan1 == 'red' and yuan2 == 'blue':
    print('purple')
elif yuan2 == 'red' and yuan1 == 'blue':
    print('purple')
elif yuan1 == 'red' and yuan2 == 'yellow':
    print('orange')
elif yuan2 == 'red' and yuan1 == 'yellow':
    print('orange')
elif yuan1 == 'blue' and yuan2 == 'yellow':
    print('green')
elif yuan2 == 'blue' and yuan1 == 'yellow':
    print('green')
else:
    print('error')

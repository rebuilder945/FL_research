num = eval(input())
if num in [x for x in range(1,11)]:
    if num%2==0:
        print('black')
    else:
        print('red')
elif num in [x for x in range(11,19)]:
    if num%2==0:
        print('red')
    else:
        print('black')
elif num in [x for x in range(19,29)]:
    if num%2==0:
        print('black')
    else:
        print('red')
elif num in [x for x in range(26,37)]:
    if num%2==0:
        print('red')
    else:
        print('black')
elif num in [0]:
    print('green')

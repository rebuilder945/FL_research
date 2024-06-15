num=eval(input())
if num==0:
    print('green')
elif num in range(1,11):
    if num%2==1:
        print('red')
    else:
        print('black')
elif num in range(11,19):
    if num%2==1:
        print('black')
    else:
        print('red')
elif num in range(19,29):
    if num%2==1:
        print('red')
    else:
        print('black')
elif num in range(29,37):
    if num%2==1:
        print('black')
    else:
        print('red')
else:
    print('error')


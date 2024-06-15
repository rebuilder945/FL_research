a=eval(input())
if a in range(1,11) and a%2==0:
    print('black')
elif a in range(1,11) and a%2==1:
    print('red')
elif a in range(12,19) and a%2==0:
    print('red')
elif a in range(12,19) and a%2==1:
    print('black')
elif a in range(19,29) and a%2==1:
    print('red')
elif a in range(19,29) and a%2==0:
    print('black')
elif a in range(29,37) and a%2==0:
    print('red')
elif a in range(29,37) and a%2==1:
    print('black')
elif a==0:
    print('green')
else:
    print('error')

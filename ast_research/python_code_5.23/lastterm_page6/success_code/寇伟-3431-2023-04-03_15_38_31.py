n=input()
if n =='0':
    print('green')
elif n in list(range(1,11)) or n in list(range(19,29)):
    if n%2==1:
        print('red')
    else:
        print('black')
elif n in list(range(11,19)) or n in list(range(29,37)):
    if n%2==0:
        print('red')
    else:
        print('black')
else:
    print('error')

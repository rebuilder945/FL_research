x=eval(input())
if x%2!=0 and (x in range(1,11) or x in range(19,29)):
    print('red')
elif x%2!=0 and (x in range(11,18) or x in range(29,37)):
    print('black')
elif x%2==0 and (x in range(1,11) or x in range(19,29)):
    print('red')
elif x%2==0 and (x in range(11,18) or x in range(29,37)):
    print('black')
elif x==0:
    print('green')
else:
    print('error')

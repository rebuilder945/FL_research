n=int(input())
if n<=5 and n>=3:
    print('spring')
elif n<=8 and n>=6:
    print('summer')
elif n<=11 and n>=9:
    print('autumn')
elif n==12 or n==1 or n==2:
    print('winter')
else:
    print('error')

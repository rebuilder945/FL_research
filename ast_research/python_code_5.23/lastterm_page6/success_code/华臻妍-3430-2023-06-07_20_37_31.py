n=eval(input())
if n==0:
    print('error')
elif n in range(1,3):
    print('winter')
elif n in range(3,6):
    print('spring')
elif n in range(6,9):
    print('summer')
elif n in range(9,12):
    print('autumn')
elif n==12:
    print('winter')
else:
    print('error')

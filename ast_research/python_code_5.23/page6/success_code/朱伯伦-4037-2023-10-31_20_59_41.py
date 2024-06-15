n=eval(input())
if n in range(3,6):
    print('spring')
elif n in range(6,9):
    print('summer')
elif n in range(9,12):
    print('winter')
elif n==12 or n in range(1,3):
    print('winter')
else:
    print('error')

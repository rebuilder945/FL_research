a=eval(input())
if a in range(3,6):
    print('spring')
elif a in range(6,9):
    print('summer')
elif a in range(9,12):
    print('autumn')
elif a==12 or a in range(1,3):
    print('winter')
else:
    print('error')

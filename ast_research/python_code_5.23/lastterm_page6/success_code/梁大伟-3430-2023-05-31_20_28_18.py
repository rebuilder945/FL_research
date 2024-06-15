s=eval(input())
if s in range(3,6):
    print('spring')
elif s in range(6,9):
    print('summer')
elif s in range(9,12):
    print('autumn')
elif s in [12,1,2]:
    print('winter')
else:
    print('error')

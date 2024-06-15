month=eval(input())
if month not in range(1,13):
    print('error')
elif month in range(3,6):
    print('spring')
elif month in range(6,9):
    print('summer')
elif month in range(9,12):
    print('autumn')
else:
    print('winter')




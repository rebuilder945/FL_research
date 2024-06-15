a=eval(input())
if a in range(1,13):
    if a in range(3,6):
        print('spring')
    if a in range(6,9):
        print('summer')
    if a in range(9,12):
        print('autumn')
    if a==12 or a==1 or a==2:
        print('winter')
else:
    print('error')

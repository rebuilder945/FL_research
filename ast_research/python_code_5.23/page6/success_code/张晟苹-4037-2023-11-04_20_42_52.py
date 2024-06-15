a=int(input())
if a>12 or a<1:
    print('error')
else:
    if a in range(3,6):
        print('spring')
    if a in range(6,9):
        print('summer')
    if a in range(9,12):
        print('autumn')
    else:
        print('winter')

a=int(input())
m=0
if a in range(1,13):
    m=1
if m==0:
    print('error')
if a in range(3,6):
    print('spring')
elif a in range(6,9):
    print('summer')
elif a in range(9,12):
    print('autumn')
elif a in range(1,3) or a==12:
    print('winter')

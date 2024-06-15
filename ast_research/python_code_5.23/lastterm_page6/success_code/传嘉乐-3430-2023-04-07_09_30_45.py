m=int(input())
if 2<m<6:
    print('spring')
elif 5<m<9:
    print('summer')
elif 8<m<12:
    print('autumn')
elif m==12 or m==1 or m==2:
    print('winter')
else:
    print('error')

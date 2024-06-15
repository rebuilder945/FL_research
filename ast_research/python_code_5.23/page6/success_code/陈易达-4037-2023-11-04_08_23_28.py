n = eval(input())
if 2<n<6:
    print('spring')
elif 5<n<9:
    print('summer')
elif 8<n<12:
    print('autumn')
elif n == 12 or 0<n<3:
    print('winter')
else:
    print('error')

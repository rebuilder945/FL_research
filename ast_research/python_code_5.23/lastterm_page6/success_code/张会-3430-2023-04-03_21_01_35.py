m = eval(input())
if m<1 or m>12:
    print('error')
else:
    if 2<m<6:
        print('spring')
    elif 5<m<9:
        print('summer')
    elif 8<m<12:
        print('autumn')
    else:
        print('winter')

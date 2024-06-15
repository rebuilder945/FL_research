n=eval(input())
if 1<=n<=12:
    if n in [3,4,5]:
        print('spring')
    if n in [6,7,8]:
        print('summer')
    if n in [9,10,11]:
        print('autumn')
    if n in[12,1,2]:
        print('winter')
else:
    print('error')

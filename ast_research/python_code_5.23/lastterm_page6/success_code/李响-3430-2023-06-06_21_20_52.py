n = eval(input())
sp = {3,4,5}
su = {6,7,8}
au = {3,10,11}
wi = {12,1,2}
if n<1 or n>12:
    print('error')
elif n in sp:
    print('spring')
elif n in su:
    print('summer')
elif n in au:
    print('autumn')
elif n in wi:
    print('winter')

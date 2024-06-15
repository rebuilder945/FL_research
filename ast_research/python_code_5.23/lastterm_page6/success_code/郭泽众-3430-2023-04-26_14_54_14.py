num = int(input())
sp = {3, 4, 5}
su = {6, 7, 8}
au = {9, 10, 11}
wi = {12, 1, 2}
if num in sp:
    print('spring')
elif num in su:
    print('summer')
elif num in au:
    print('autumn')
elif num in wi:
    print('winter')
else:
    print('error')

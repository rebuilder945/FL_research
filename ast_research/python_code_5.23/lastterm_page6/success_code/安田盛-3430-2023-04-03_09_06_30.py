n=eval(input())
a=[3,4,5]
b=[6,7,8]
c=[9,10,11]
d=[12,1,2]
if n<1 or n>12:
    print('error')
elif n in a:
    print('spring')
elif n in b:
    print('summer')
elif n in c :
    print('autumn')
else:
    print('winter')

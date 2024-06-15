x1=[3,4,5]
x2=[6,7,8]
x3=[9,10,11]
x4=[12,1,2]
n=eval(input())
if n not in range(1,13):
    print('error')
elif n in x1:
    print('spring')
elif n in x2:
    print('summer')
elif n in x3:
    print('autumn')
else:
    print('winter')


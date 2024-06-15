a=input()
n=0
m=0
w=0
z=0
y=0
for x in a:
    if x.isdigit():
        n=1
    elif x.isalpha():
        if x.isupper():
            m=1
        if x.islower():
            w=1
    else:
        y=1
    if len(a)>=8:
        z=1
if n+m+w+z+y==1:
    print('1')
elif n+m+w+z+y==2:
    print('2')
elif n+m+w+z+y==3:
    print('3')
elif n+m+w+z+y==4:
    print('4')
elif n+m+w+z+y==5:
    print('5')

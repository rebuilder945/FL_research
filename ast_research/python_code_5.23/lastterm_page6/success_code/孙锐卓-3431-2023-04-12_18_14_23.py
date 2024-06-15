a=eval(input())
if a<0 or a>36:
    print('error')
b=[x for x in range(1,11) if x%2==1]
c=[x for x in range(1,11) if x%2==0]
d=[x for x in range(11,19) if x%2==1]
e=[x for x in range(11,19) if x%2==0]
f=[x for x in range(19,29) if x%2==1]
h=[x for x in range(19,29) if x%2==0]
i=[x for x in range(29,37) if x%2==1]
j=[x for x in range(29,37) if x%2==0]
if a==0:
    print('green')
elif a in b:
    print('red')
elif a in e:
    print('red')
elif a in f:
    print('red')
elif a in j:
    print('red')
elif a in c:
    print('black')
elif a in d:
    print('black')
elif a in h:
    print('black')
elif a in i:
    print('black')



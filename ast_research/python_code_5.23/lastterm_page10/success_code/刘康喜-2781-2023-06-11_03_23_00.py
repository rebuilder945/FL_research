a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
f=len(a)-1
for i in range(0,f):
    q=int(a[i])
    w=int(b[i])
    c=c+q*w

d=c%11
d=(12-d)%11
if d==10 and a[-1]=='X':
    print('Correct')
elif a[-1]!='X'and int(a[-1])==d:
    print('Correct')
elif len(a)!=18:
    print('Error')
else:
    print('Wrong')


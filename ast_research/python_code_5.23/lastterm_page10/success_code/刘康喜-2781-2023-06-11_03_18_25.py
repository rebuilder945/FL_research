a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
f=len(a)-1
for i in range(0,f):
    q=int(a[i])
    w=int(b[i])
    c=c+q*w

d=c%11

m=[x for x in range(0,11)]
n=[1,0,'X',9,8,7,6,5,4,3,2]
for i in m:
    if m[i]==d:
        d=n[i]


if d==10 and a[-1]=='X':
    print('Correct')
if a[-1]!='X' and int(a[-1])==d:
    print('Correct')
elif len(a)!=18:
    print('Error')
else:
    print('Wrong')


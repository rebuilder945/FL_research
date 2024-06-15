a=list(input())
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
p='10x98765432'
c=list(p)
d=[0,1,2,3,4,5,6,7,8,9,10]
e={}
for i in range(11):
    e[d[i]]=c[i]
if len(a)==18:
    for i in range(17):
        m=0
        m+=eval(a[i])*b[i]
    n=m%11
    print(e[n])
    if e[n]==a[-1]:
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')


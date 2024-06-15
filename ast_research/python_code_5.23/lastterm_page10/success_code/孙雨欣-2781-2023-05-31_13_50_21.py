a=list(input())
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
if len(a)!=18:
    print('Error')
else:
    if a[-1]=='X':
        m=10
    else:
        m=a[-1]
    for i in range(len(a)-1):
        sum+=int(a[i])*b[i]
        n=sum%11
    if m!=(12-n)%11:
        print('Wrong')
    else:
        print('Correct')

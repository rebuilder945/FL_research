s=input()
a=s[-1]
if len(s)!=18:
    print('Error')
else:
    s1=[int(s[i]) for i in range(len(s)-1)]
    s2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum=0
    for i in range(17):
        sum+=(s1[i])*(s2[i])
    n=sum%11
    if n==2 and a=='X':
        print('Correct')
    elif a==n:
        print('Correct')
    else:
        print('Wrong')

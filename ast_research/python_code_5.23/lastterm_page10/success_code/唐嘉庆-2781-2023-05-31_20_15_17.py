a=str(input())
if len(a)!=18:
    print('Error')
else:
    s=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum=0
    for i in range(len(a)-1):
        sum+=int(a[i])*s[i]
    n=sum%11
    m=(12-n)%11
    if m==10 and a[-1]=='X':
        print('Correct')
    if m!=10 and m==int(a[-1]):
        print('Correct')
    if m!=10 and m!=int(a[-1]):
        print('Wrong')
        




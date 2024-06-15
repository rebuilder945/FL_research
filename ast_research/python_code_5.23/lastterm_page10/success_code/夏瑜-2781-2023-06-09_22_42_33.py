a=list(input())
if len(a)!=18:
    print("Error")
else:
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum=0
    for x in range(17):
        sum +=int(a[x])*num[x]
    n=sum%11
    s=['1','0','X','9','8','7','6','5','4','3','2']
    m=s[n]
    if a[-1]==m:
        print('Correct')
    else:
        print('Wrong')






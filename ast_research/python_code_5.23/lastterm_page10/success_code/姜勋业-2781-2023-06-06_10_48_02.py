a=list(input())
b=[7,9,0,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
k=0
if len(a)!=18:
    print('Error')
else:
    for i in range(0,len(b)):
        k=k+eval(a[i])*(b[i])
    q=k%11
    m=(12-q)%11
    if a[17]=='X' and m==10:
        print('Corrct')
    elif eval(a[17])==m:
        print('Corrct')
    else:
        print('Wrong')

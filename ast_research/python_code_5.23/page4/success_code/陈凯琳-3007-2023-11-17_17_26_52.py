a=eval(input())
n,m=eval(input())
lit=[]
if  m<n or n>=len(a):
    print('error')
else:
    b=a[n:m]
    for i in a:
        if i not in b:
            lit.append(i)
    print(lit)





     

    



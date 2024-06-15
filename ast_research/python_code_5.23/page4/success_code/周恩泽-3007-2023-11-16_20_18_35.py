n1=eval(input())
n2,n3=eval(input())
if n2<=n3 and 0<n2<len(n1) and 0<n3<len(n1):    
    for x in range(n2,n3):
        n1.pop(x)
    print(n1)
else:
    print("error")




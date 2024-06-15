a=eval(input())
a.sort()
a.reverse()
if a[0]!=0:
    e=str(a[0])
    for x in range(len(a)-1):
        d=str(a[x+1])
        e=e+d
        print(e)
else:
    print(a[0])
    

    
    
    

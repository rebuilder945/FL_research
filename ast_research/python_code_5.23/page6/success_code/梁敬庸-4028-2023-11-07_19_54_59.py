def det(n):
    
    for x in range(2,int(n/2)+1):
        if n%x==0 and x!=i:
            return False
          
    return True
m=eval(input())
b=[]
if m<=1 or type(m)!=int:
    print("illegal input")
else:
    for i in range(2,m+1):
        if det(i):
            i=str(i)
            if i[:]==i[::-1]:
                b.append(i)
    for o in b:
        print(o,end=" ")




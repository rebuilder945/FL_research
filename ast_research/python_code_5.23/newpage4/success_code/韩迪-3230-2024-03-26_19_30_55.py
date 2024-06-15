
from re import A


a=list(eval(input()))
a.sort(reverse=True)
if a[0]==0:
    print("0")
for i in a:      
    if a[0]!=0:
        
        print(i,end="")
    else:
        pass




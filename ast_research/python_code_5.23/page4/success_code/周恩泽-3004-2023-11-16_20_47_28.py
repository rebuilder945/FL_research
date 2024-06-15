n1=eval(input())
n2=[]
for x in n1:
    for y in range(2,x):
        if x%y==0:
            break
    else:
        n2.append(x)
if 1 in n2:
    n2.remove(1)
print(n2)
        
    

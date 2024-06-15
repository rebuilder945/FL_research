x=eval(input())
x1=list(reversed(x))
for i in x:
    if  x1.count(i)>1:
        x.remove(i)
        
   
print(x)


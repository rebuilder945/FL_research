x=eval(input())
x2=x.copy()
for i in x:
    if x.count(i)>1 and x2.count(i)>1:
        x2.remove(i)
       
    
print(x2)


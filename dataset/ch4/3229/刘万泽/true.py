a=eval(input())
b=[]
for i in a:
    t=a.count(i)
    if t==1:
       b.append(i)
    else:
        continue
b.sort()    
if b==[]:
    print("False") 
else:
    x=b
    print(*x,sep=',')
           

    

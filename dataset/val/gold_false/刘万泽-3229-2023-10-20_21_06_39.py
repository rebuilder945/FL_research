a=eval(input())
b=[]
for i in a:
    t=a.count(i)
    if t>1:
       b.append(i)
    else:
        continue
if b==[]:
    print("False") 
else:
    print(str(b))       

    

aug=eval(input())
b=[]
for x in aug:
    if aug.count(x)==1:
        b.append(x)
b.sort()
if b==[]:
    print("False")
else:
    for i in b[:-1]:
        print(i,end=",")    
    print(b[-1])
        

ls=eval(input())
l=[]
for x in ls:
    if ls.count(x)== 1:
        l.append(x)
if len(l) == 0:
    print("False")
else:
    l.sort()
    y=str(l)
    print(y)




    

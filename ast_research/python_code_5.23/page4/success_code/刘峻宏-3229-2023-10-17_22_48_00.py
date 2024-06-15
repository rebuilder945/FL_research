a=eval(input())
b=[]
i=0
while True:
    name=a.pop(i)
    if name in a:
        a.insert(i,name)
    else:
        a.insert(i,name)
        b.append(name)
    i+=1    

    if a==[]:
        break
if b==[]:
    print("False")
else:
    b.sort()
    print(str(b))

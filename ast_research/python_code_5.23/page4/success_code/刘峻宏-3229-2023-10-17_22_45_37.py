a=eval(input())
b=[]
i=0
while True:
    name=a.pop(0)
    if name in a:
        pass
    else:
        
        b.append(name)
        

    if a==[]:
        break
if b==[]:
    print("False")
else:
    b.sort()
    print(str(b))

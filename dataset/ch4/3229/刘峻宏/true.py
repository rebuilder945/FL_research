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

    if i>=len(a):
        break
if b==[]:
    print("False")
else:
    
    b.sort()
    
    s=str(b)[1:-1].split(" ")
    while True:

        if "," in s:
            s.remove(",")
        else:
            break
    
    s="".join(str(e)for e in s)
    print(s)
    
    



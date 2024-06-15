item=input()or "q"
a=[]
b=0
while item!="q":
    a.append(item)
    for i in a:
        a.remove(i)
        for j in a:
            if i==j:
                b+=1
print(i,b)                


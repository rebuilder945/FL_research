a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[eval(q) for q in a.split(",")]
br=b.reverse()
p=[]
for el in br:
    if p.count(el)<1:
        p.append(el)
pr=p.reverse()

    
print(pr) 

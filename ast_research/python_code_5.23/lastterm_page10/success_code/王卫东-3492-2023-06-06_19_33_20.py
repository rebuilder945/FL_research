n=[x for x in input()]
m=n.copy()
if n==[]:
    print("None")
else:
    for x in n:
        if n.count(x)>1:
            m.remove(x)
    print(m[0])    

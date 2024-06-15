t=input()
t=t.replace("[","").replace("]","")
t=t.split(',')
t=list(t)
p=[]
for i in t:
    if i not in p:
        p.append(i)
print(p)
        

t=eval(input())
t.reverse()
p=[]
for i in t:
    if i not in p:
        p.append(i)
p.reverse()
print(p)
        

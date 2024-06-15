a=eval(input())
for x in a:
    if a.count(x)>1:
        a.remove(x)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
    

            



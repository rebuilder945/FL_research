a=list(eval(input()))
j=[]
for i in a:
    if a.count(i)!=1:
        a.remove(i)
    else:
        j.append(i)
print(j)

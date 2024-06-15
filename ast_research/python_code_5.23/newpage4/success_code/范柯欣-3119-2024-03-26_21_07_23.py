m=list(eval(input())) 
for i in m:
    while m.count(i)>1:
        m.remove(i)
        i-=1
print(m)

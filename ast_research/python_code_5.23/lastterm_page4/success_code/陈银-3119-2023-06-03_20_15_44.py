lst = eval(input())
lst.reverse()
m=[]
for i in lst:
    if i not in m:
        m.insert(0,i)
print(m)

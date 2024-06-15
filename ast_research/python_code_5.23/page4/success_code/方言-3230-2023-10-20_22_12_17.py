list=eval(input())
sz=0
for i in range(len(list)):
    m=max(list)
    sz=sz*10+m
    list.remove(m)
print(sz)

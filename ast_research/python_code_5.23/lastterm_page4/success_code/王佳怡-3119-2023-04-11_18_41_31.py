l=list(eval(input()))
l.reverse()
l2=[]
for i in l:
    if i not in l2:
        l2.insert(0,i)
print(l2)


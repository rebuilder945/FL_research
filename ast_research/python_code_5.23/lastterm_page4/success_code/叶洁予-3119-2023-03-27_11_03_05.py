l1=eval(input())
l1.reverse()
l2=[]
for i in l1:
    if i not in l2:
        l2.insert(0,i)
print(l2)

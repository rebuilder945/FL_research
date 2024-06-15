lst=eval(input())
lst1=[]
for i in lst:
    for s in range(2,i):
        if i%s==0:
            lst1.append(i)
            if lst1.count(i)!=i-2:
                lst.remove(i)
print(lst)


lst=eval(input())
lst2=[]
for i in lst:
    if i>=2:
        for t in range(2,i):
            if i%t != 0:
                lst2.append(i)
print(lst2)

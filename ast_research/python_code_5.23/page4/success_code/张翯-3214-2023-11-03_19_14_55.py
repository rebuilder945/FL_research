lst=eval(input())
lst2=[]
for i in lst:
    if i == 0:
        lst2.append(i)
        lst.remove(i)
print(lst+lst2)


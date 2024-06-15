lst=eval(input())
lst2=lst.count(0)
for x in range(lst.count(0)):
    lst.remove(0)
    lst.append(0)
print(lst)

lst=eval(input())
lst2=[]
for i in lst:
    if i == 0:
        lst2.append(i)
while 0 in lst:
    lst.remove(0)
print(lst+lst2)


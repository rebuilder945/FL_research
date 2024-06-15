lst=eval(input())
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst2.append(i)
        lst.reverse
        print(lst2)
    elif lst.count(i)>=2:
        print(False)


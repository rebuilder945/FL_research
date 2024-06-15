lst=eval(input())
lst1=lst.copy()
for i in lst:
    a=lst1.count(i)
    if a>1:
        for x in range(1,a):
            lst1.remove(i)
print(lst1)
            



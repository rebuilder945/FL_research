lst=eval(input())
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst2.append(i)
if lst2==[]:
    print(False)
else:
    print(str(lst2)).sort(reverse=False)

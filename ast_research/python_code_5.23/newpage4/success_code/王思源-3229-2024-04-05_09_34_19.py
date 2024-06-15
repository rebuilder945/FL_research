lst1=eval(input())
lst2=[]
for x in lst1:
    if lst1.count(x)==1:
        lst2.append(x)
lst2.sort()
if len(lst2)==0:
    print("error")
else:
    str1=",".join(map(str,lst2))
    print(str1)
   



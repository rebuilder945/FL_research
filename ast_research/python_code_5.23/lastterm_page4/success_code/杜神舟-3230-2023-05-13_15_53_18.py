list1=eval(input())
list1.reverse()
list2=[]
for x in list1:
    c=str(x)
    list2.append(c)
dd=int(''.join(list2))
print(dd)

list1=eval(input())
list1.sort()
list2=list1.copy()
list2.reverse()
f1=''
for i in list2:
    f1+=str(i)+""
print(f1)



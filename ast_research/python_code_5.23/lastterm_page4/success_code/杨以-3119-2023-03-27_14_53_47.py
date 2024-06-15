list=eval(input())
list2=list.copy()
for a in list2:
  if list.count(a)>1:
    list.remove(a)
print(list)



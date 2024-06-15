list1=eval(input())
list2=list(set(list1))
a=max(list2)
b=min(list2)
list2.remove(a)
list2.remove(b)
print(list2)


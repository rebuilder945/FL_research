list=eval(input())
a=max(list)
b=min(list)
while a in list:
    list.remove(a)
while b in list:
    list.remove(b)
print(list)

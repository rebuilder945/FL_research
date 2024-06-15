list=eval(input())
max=max(list)
min=min(list)
while max in list:
    list.remove(max)
while min in list:
    list.remove(min)
print(list)


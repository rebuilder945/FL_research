list=eval(input())
a=max(list)
b=min(list)
for x in list:
    if x==a or x==b:
        list.remove(x)
print(list)


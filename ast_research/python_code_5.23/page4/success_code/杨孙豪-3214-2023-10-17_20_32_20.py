lst=eval(input())
b=lst.count(0)
for i in range(b):
    lst.remove(0)
for i in range(b):
    lst.append(0)
print(lst)

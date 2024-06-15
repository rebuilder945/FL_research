lst=eval(input())
for i in range(lst.count(max(lst))):
    lst.remove(max(lst))
for i in range(lst.count(min(lst))):
    lst.remove(min(lst))
print(lst)

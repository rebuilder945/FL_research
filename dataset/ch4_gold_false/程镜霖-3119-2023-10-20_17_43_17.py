lst=eval(input())
for i in lst:
    for x in range(lst.count(i)-1):
        lst.remove(i)
print(lst)

lst=eval(input())
lst.sort()
for i in lst[:]:
    while lst.count(i)>1:
        lst.remove(i)
print(lst)

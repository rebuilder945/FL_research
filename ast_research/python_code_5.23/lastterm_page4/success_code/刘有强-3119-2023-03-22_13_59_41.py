lst=eval(input())
k=0
for i in range(len(lst)):
    while lst.count(i)>1:
        lst.remove(i)
print(lst)

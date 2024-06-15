lst=eval(input())
min=min(lst)
max=max(lst)
lst2=lst.copy()
for i in range(len(lst)):
    if lst[i]==min or lst[i]==max:
        lst2.remove(lst[i])
print(lst2)

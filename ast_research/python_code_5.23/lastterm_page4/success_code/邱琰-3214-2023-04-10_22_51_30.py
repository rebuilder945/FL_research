lst=eval(input())
for i in len(lst):
    if lst[i]==0:
        lst.remove(lst[i])
        lst.append(0)
print(lst)

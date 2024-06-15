lst=eval(input())
lst1=lst.copy()
for i in lst:
    if i==max(lst) and i==min(lst):
        lst1.remove(i)
print(lst1)


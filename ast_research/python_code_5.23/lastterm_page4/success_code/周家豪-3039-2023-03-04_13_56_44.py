lst=eval(input())
maximum=max(lst)
minimum=min(lst)
lst2=lst.copy()
for i in lst2:
    if maximum in lst:
        lst.remove(maximum)
    if minimum in lst:
        lst.remove(minimum)

print(lst)

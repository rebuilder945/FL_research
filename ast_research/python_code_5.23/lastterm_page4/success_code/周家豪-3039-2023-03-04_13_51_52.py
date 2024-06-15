lst=eval(input())
maximum=max(lst)
minimum=min(lst)

for i in lst:
    if maximum in lst:
        lst.remove(maximum)
    if minimum in lst:
        lst.remove(minimum)

print(lst)

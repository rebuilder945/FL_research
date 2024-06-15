a=input()
lst=eval(a)
min=min(lst)
max=max(lst)
b=[x for x in lst if x != min and x !=max]
print(b)

lst = eval(input())
iMax = max(lst)
iMin = min(lst)
while iMax in lst:
    lst.remove(iMax)
    pass
while iMin in lst:
    lst.remove(iMin)
    pass
print(lst)

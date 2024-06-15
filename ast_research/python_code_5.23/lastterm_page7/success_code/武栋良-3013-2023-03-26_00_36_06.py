lst = input().split()
GDP = {}
while "ok" not in lst:
    GDP[lst[0]] = int(lst[1])
    lst = input().split()
lst1 = list(GDP.keys())
lst1.sort()
lst2 = list(GDP.values())
lst2.sort()
print(lst1)
print(lst2)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(list(GDP.values())))




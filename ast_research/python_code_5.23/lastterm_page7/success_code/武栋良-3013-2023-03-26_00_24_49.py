lst = input().split()
GDP = {}
while "ok" not in lst:
    GDP[lst[0]] = int(lst[1])
    lst = input().split()
print(list(GDP.keys()))
print(list(GDP.values()))
if "india" in GDP:
    print("yes")
else:
    print("no")
print(sum(list(GDP.values())))




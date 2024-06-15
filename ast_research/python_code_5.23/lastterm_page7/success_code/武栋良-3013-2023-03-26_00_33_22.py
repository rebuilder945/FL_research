lst = input().split()
GDP = {}
while "ok" not in lst:
    GDP[lst[0]] = int(lst[1])
    lst = input().split()
print(list(GDP.keys()).sort())
print(list(GDP.values()).sort())
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(list(GDP.values())))




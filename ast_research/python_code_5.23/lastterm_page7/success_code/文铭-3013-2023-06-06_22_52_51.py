s = str(input())
d = {}
while s != "ok":
    lst = s.split(" ")
    d[lst[0]]= lst[1]
    s = str(input())
print(list(d.keys()))
print(list(d.values()))
if "india" in d:
    print("yes")
else:
    print("no")
print(sum(d.values()))

s = str(input())
d = {}
while s != "ok":
    lst = s.split(" ")
    d[lst[0]]= int(lst[1])    
    s = str(input())
k = list(d.keys())
k.sort()
v = list(d.values())
v.sort()
print(k)
print(v)
if "India" in d:
    print("yes")
else:
    print("no")
print(sum(d.values()))

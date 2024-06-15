s = str(input())
d = {}
while s != "ok":
    lst = s.split(" ")
    d[lst[0]]= int(lst[1])    
    s = str(input())
print(list(d.keys()))
print(list(d.values()))
if "India" in d:
    print("yes")
else:
    print("no")
print(sum(d.values()))

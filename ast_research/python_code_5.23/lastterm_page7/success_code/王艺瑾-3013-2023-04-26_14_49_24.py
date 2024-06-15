GDP={}
while True:
    x=input()
    if x=="ok":
        break
    a,b=x.split(" ")
    GDP[a]=int(b)
keys=list(GDP.keys())
values=list(GDP.values())
keys.sort()
values.sort()
print(keys)
print(values)
print("yes" if "India" in keys else "no")
print(sum(values))

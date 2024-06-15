data=[]
while True:
    a=input()
    if a== "ok":
        break
    else:
        b,c=a.split()
        data.append((b,c))
data=dict(data)
name=list(data.keys())

country = list(data.keys())
num = list(data.values())

print(country.sort())
print(num.sort())
for i in country:
    if i =="India":
        print("yes")
    else:
        print("no")
print(sum(num))


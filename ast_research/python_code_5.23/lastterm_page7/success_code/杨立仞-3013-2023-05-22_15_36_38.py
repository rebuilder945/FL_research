data=[]
while True:
    a=input()
    if a== "ok":
        break
    else:
        b,c=a.split()
        c=int(c)
        data.append((b,c))
data=dict(data)
country=list(data.keys())
country.sort()
num=list(data.values())
num.sort()
print(country)
print(num)
for i in country:
    if i =="India":
        print("yes")
    else:
        print("no")
print(sum(num))


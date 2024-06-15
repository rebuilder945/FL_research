ls=[]
ls1=[]
GDP={}
country,G=input().split()
ls.append(country)
ls1.append(eval(G))
while True:
    a=input()
    if a=="ok":
        break
    else:
        country,G=a.split(" ")
    ls.append(country)
    ls1.append(eval(G))
for i in ls:
    GDP[i]=GDP.keys()
for x in ls1:
    GDP[i]=x
ls.sort()
ls1.sort()
print(ls)
print(ls1)
if "India" in GDP.keys():
    print("yes")
else:
    print("no")
a=0
for i in ls1:
    a=a+i
print(a)

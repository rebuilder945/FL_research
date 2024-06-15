a=input()
GDP={}
while a!="ok":
    a,d=map(str,a.split(' '))
    GDP[a]=int(d)
    a=input()
n=[]
m=[]
for i in GDP.keys():
    n.append(i)
for i in GDP.values():
    m.append(i)
m.sort()
n.sort()
print(n)
print(m)
if "India"in GDP:
    print("yes")
else:
    print("no")
print(sum(m))



       



                    





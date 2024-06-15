a=input()
GDP={}
while a!="ok":
    a,d=map(str,a.split(' '))
    GDP[a]=int(d)
    a=input()
n=GDP.keys()
m=GDP.values()
print(n.sort())
print(m.sort())
if "India"in GDP:
    print("yes")
else:
    print("no")
print(sum(m))



       



                    





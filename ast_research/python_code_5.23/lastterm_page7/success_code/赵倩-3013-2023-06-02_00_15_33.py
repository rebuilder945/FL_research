a=input()
GDP={}
while a!="ok":
    a,d=map(str,a.split(' '))
    GDP[a]=int(d)
    a=input()
n=a.keys()
m=a.values()
print(n.sort())
print(m.sort())
if "India"in GDP:
    print("yes")
else:
    print("no")
print(sum(m))



       



                    





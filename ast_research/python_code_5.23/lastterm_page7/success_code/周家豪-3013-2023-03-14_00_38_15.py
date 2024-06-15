lst0=input()
gdp={}
lst1,lst2=[],[]
while lst0!="ok":
    k,v=lst0.split(" ")
    gdp[k]=eval(v)
    lst1.append(k)
    lst2.append(eval(v))
    lst0=input()
lst1.sort()
lst2.sort()

print(lst1)
print(lst2)
if "India" in gdp :
    print("yes")
else:
    print("no")
print(sum(lst2))

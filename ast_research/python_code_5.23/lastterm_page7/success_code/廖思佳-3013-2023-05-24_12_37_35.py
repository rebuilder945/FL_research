
s='no'
GDP={}
while True:
    n=input()
    if n=="ok":
        break
    nation,gpa=n.split()
    GDP[nation]=int(gpa)
    if nation=="India":
        s="yes"

list1=sorted(list(GDP.keys()))
list2=sorted(list(GDP.values()))
a=sum(list2)

print(list1)
print(list2)
print(s)
print(a)

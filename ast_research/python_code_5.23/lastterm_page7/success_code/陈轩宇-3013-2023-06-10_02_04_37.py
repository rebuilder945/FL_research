dic1={}
a = input()
while a!='ok':
    name,gdp = a.split(" ")
    gdp = eval(gdp)
    dic1[name] = gdp
    a = input()
list1 = list(dic1.keys())
list1.sort()
list2 = list(dic1.values())
list2.sort()
c = sum(list2)
print(list1)
print(list2)
if 'India' in dic1:
    print('yes')
else:
    print('no')
print(c)

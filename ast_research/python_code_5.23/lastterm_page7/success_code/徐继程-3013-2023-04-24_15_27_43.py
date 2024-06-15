item=input()or"ok"
GDP={}
while(item!="ok"):
    name,gdp=item.split()
    gdp=eval(gdp)
    GDP.update({name:gdp})
    item=input()or"ok"
list1=[]
list2=[]
for i in GDP:
    list1.append(i)
    list2.append(GDP.get(i))
list1.sort()
list2.sort()
print(list1)
print(list2)
if 'India' in GDP:
    print('yes')
else:
    print('no')

print(sum(list2))

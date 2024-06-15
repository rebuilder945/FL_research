GDP=input() or 'ok'
dic={}
while (GDP != 'ok'):
    name,gdp = GDP.split()
    gdp=eval(gdp)
    dic[name]=gdp
    GDP = input() or 'ok'
lst1=list(dic.keys())
lst2=list(dic.values())
if 'India' in lst1:
    kim = 'yes'
else:
    kim = 'no'
x=sum(lst2)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
print(kim)
print(x)

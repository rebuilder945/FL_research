ls=input().split()
GDP = {}
while ls!=["ok"]:
    v,k = ls
    GDP.setdefault(v,k)
    ls=input().split()
print(list(GDP.keys()))
value=[]
for i in GDP.values():
    a = int(i)
    value.append(a)
value.sort()
print(value)
if 'India' not in GDP.keys():
    print('no')
else:
    print('yes')
s = sum(value)
print(s)

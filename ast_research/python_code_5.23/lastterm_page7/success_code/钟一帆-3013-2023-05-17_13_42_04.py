GDP={}
s=input().split(' ')
while "ok" not in s:
    keys=s[0]
    values=int(s[1])
    GDP[keys]=values
    s=input().split(' ')
countries=[]
num=[]
for i in GDP.keys():
    countries.append(i)
countries.sort(reverse=False)
for x in GDP.values():
    num.append(x)
num.sort(reverse=False)
print(countries)
print(num)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(num))

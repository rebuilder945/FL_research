dic={}
string=input() or 'ok'
while string!='ok':
    lst=string.split(' ')
    dic[lst[0]]=eval(lst[-1])
    string=input() or 'ok'
country=list(dic.keys())
country.sort()
if 'India' in country:
    t='yes'
else: t='no'
GDP=list(dic.values())
GDP.sort()
print(country,GDP,t,sum(GDP),sep='\n')

gdp={}
i=input()
while i!="ok":
    a,b=map(str,i.split(' '))
    gdp[a]=int(b)
    i=input()
gdp['China']=95
del gdp['Japan']
print(len(gdp))
print(gdp['USA'])


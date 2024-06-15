n=input().split( )
GDP = []
while True:
    if n!=['ok']:
        GDP.append(n)
        n=input().split( )
    else:
        break
gdp=dict(GDP)

keylist=[]
valuelist=[]
for k,v in gdp.items():
    keylist.append(k)    
    valuelist.append(int(v))
keylist.sort()
valuelist.sort()
print(keylist)
print(valuelist)
if 'India' not in keylist:    
    print("no")
else:    
    print("yes")
print(sum(valuelist))

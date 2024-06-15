ls1=[]
while True:
    ls=input().split()
    if ls==['ok']:
        break
    else:
        ls1.append(ls)
guo=[]
GDP=[]
for x in ls1:
    guo.append(x[0])
    GDP.append(int(x[1]))
print(gou)
print(GDP)
if 'India' in guo:
    print("yes")
else:
    print("no")
print(sum(GDP))

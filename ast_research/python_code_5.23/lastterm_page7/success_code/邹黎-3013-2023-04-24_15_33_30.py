GDP={}
while True:
    c=input()
    if c!="ok":
        a,b=c.split()
        GDP[a]=eval(b)
    else:
        break
lstkey=[]
lstvalue=[]
for x,y in GDP.items():
    lstkey.append(x)
    lstvalue.append(y)
lstkey.sort()
lstvalue.sort()
def panduan(x,dic):
    if x in dic.keys():
        return("yes")
    else:
        return("no")
print(lstkey)
print(lstvalue)
print(panduan('India',GDP))
print(sum(lstvalue))




str=input() or "ok"
dic={}
ls=[]
i=0
while str!="ok":
    ls+=str.split()
    dic[ls[i]]=int(ls[i+1])
    i+=2
    str=input() or "ok"
keys=list(dic.keys())
values=list(dic.values())
print(sorted(keys))
print(sorted(values))
if 'India' in dic.keys():
    print("yes")
else:
    print("no")
print(sum(list(dic.values())))

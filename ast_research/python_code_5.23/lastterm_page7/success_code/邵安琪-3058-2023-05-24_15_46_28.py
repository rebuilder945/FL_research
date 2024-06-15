keys=input()
dic={}
while keys !="q":
    dic[keys]=dic.get(keys,0)+1
    keys=input()
a=max(dic.values())
keylist=[]
valuelist=[]
for key,value in dic:
    keylist.append(key)
    valuelist.append(value)
key1=keylist[valuelist.index(a)]
print(key1,a)

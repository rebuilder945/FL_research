a=input()
dic={}
while a!='q':
    if a not in dic:
        
        dic[a]=1
    else:
        dic[a]+=1
    a=input()
while a=="q":
    break
m=max(dic.values())
for k,v in dic.items():
    if v==m:
        print(k,v)
 
# print(dic)
# dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# print(dic)
# print( str(dic[0:1]),end="")


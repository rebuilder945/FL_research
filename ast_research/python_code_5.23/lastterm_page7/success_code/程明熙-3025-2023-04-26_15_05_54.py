from posixpath import split


a=input().split()
a.sort()
dic={}
# print(a)
for i in a:
    if i not in dic:
        
        dic[i]=1
    else:
        dic[i]+=1
    
# while a==None:
#     break

m=max(dic.values())
for k,v in dic.items():
    if v==m:
        print(k,v)
 
# print(dic)
# dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# print(dic)
# print( str(dic[0:1]),end="")


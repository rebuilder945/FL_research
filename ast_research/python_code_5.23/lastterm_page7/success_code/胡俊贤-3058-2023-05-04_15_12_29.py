s=str(input())
ls=[]
dict1={}
while s!='q':
    if s in ls:
        dict1[s]=dict1[s]+1
        s=str(input())
    else:
        ls.append(s)
        dict1[s]=1
        s=str(input())
ls1=[]
for k,v in dict1.items():
    ls1.append([k,v])
ls1.sort(key=lambda x:x[1],reverse=True)
print(ls1[0][0],ls1[0][1])
        



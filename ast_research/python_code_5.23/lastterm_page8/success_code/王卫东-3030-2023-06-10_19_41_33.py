a=input().split(',')

b=list(eval(input()))
dic={}
c=[]
for x in range(len(a)):
    dic[a[x]]=dic.get(a[x],b[x])
for k,v in dic.items():
    c.append([k,v])
c.sort(key=lambda x:x[-1])    
print(c)






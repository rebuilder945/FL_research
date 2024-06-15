a=input().split()
dic={"english":1,"python":2,"math":3}
for i in dic.items():
    dic[i[0]]=a[i[1]]
dic=dict(sorted(dic.items(),key=lambda x:x[1]))
b=a[1:]
b=list(map(int,b))
average=sum(b)/len(b)
dic["average"]=average
s=" ".join(map(str,list(dic.values())))
print(a[0],s)
    

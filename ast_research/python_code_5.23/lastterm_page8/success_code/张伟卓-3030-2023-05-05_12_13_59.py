n=input().split(",")
g=list(map(int,input().split(",")))
dic={}
ls=[]
for i in range(len(n)):
    dic[n[i]]=g[i]
    ls.append(n[i])
ls.sort()
x=0
while x <len(ls):
    new=dic.get(x)
    li=[x,new]
    x+=1
new_=[]
new_.append(li)
    
print(new_)

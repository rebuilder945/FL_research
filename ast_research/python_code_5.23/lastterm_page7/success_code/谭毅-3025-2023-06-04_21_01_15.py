ls=input().split()
ls.sort()
dic={}
ls2=[]
for x in ls:
    dic[x]=dic.get(x,0)+1
    a=ls.count(x)
    if a not in ls2:
        ls2.append(a)
for x,y in dic.items():
    if y==max(ls2):
        print(x,y)

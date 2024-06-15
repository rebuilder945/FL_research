n=input()
dic={}
while n!="q":
    dic[n]=dic.get(n,0)+1
    n=input()
a=list(dic.items())
a.sort(key=lambda x:x[1])
k,v=a[-1]
print(k,v)


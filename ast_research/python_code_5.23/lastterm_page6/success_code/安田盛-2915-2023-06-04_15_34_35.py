s=eval(input())
dic={}
a=""
for i in s:
    a+=i
for i in a:
    dic[i]=dic.get(i,0)+1
lst=[]
for x,y in dic.items():
    lst.append([x,y])
lst.sort(key=lambda x:x[0])
for i in lst:
    print(*i,sep=",")
    




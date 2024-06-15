lst=input().split()
num=[]
times=[]
list.sort()
for i in lst:
    num.append((i,lst.count(i)))
    times.qppend(lst.count(i))
dic=dict(num)
for k,v in dic.items:
    if v==max(times):
        print(k,v)




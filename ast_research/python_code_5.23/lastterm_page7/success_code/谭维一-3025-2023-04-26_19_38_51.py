s=input().split(' ')
set=set(s)
count={}
for i in set:
    count[i]=s.count(i)
countsorted=sorted(count.items(),key=lambda kv:(-kv[1],kv[0]))
most=countsorted[0][1]
res=filter(lambda item: item[1] == most,countsorted)
for item in res:
    print(f"{item[0]} {item[1]}")

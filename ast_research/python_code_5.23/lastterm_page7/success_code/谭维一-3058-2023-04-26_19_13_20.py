sl=[]
while True:
    s=input()
    if s=='q':
        break
    sl.append(s)
set=set(sl)
result={}
for item in set:
    result[item]=sl.count(item)
result=sorted(result.items(),key=lambda kv:kv[1],reverse=True)
print(result[0][0],result[0][1])

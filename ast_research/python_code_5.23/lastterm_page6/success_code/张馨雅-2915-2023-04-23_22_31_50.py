s=eval(input())
count={}
for x in s:
    for i in x:
        count[i]=count.get(i,0)+1
print(count)
count=sorted(count.items(),key=lambda x:x[0])
count=[list(x) for x in count]
print(count)
for a in count:
    print('{},{}'.format(count[a][0],count[a][1]))

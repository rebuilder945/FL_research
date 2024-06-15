names=input().split(',')
scores=input().split(',')
scores=[int(x) for x in scores]
lis=[]
for index,name in enumerate(names):
    lis.append([name,scores[index]])
lis.sort(key=lambda x:x[1])
print(lis)


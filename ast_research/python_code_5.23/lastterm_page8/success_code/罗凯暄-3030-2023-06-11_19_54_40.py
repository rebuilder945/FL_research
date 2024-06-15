names=input().split(',')
scores=eval(input())
lst1,lst2=list(names),list(scores)
sum=()
zong=[]
for i in range(len(names)):
    sum=(lst1[i],lst2[i])
    zong.append(list(sum))
zong1=sorted(zong,key=lambda x:x[1])
print(zong1)


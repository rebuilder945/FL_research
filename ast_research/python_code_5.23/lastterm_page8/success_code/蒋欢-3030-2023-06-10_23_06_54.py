name=input().split(",")
num=eval(input())
sums=[]
for i in range(len(name)):
    s=[name[i],num[i]]
    sums.append(s)
sums.sort(key=lambda x:x[1])
print(sums)

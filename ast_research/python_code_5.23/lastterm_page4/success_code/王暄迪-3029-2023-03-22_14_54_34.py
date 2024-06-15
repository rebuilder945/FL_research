names=input().split(",")
score=eval(input())
names1=list(names)
sum=()
sum1=[]
for i in range(len(names)):
    sum=(names1[i],score[i])
    sum1.append(list(sum))
print(sum1)

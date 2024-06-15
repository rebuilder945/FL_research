sname=input().split(',')
score=eval(input())
sname1=[sname]
sum1=()
sum2=[]
for i in range(len(sname1)):
    sum1=(sname1[i],score[i])
    sum2.append(list(sum1))
sum2.sort(key=lambda x:x[1])
print(sum2)

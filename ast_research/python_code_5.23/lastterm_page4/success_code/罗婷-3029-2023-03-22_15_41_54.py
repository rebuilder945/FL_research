sName=input().split("'")
sGrade=eval(input())
sum1=list(sName)
sum2=()
sum3=[]
for i in range(len(sum1)):
    sum2=[sumi[i],sGrade[i]]
    sum3.append(list(sum2))
print(sum3)

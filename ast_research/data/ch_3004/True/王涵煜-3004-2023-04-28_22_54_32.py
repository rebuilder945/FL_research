from math import sqrt
num=eval(input())
num.sort()
ans=[]
for i in range(len(num)):
    if num[i]==2 or num[i]==3:
        ans.append(num[i])
    else:
        for j in range(2,int(sqrt(num[i]))+1):
            if num[i]%j==0:
                break
            if j==int(sqrt(num[i])):
                ans.append(num[i])
print(ans)


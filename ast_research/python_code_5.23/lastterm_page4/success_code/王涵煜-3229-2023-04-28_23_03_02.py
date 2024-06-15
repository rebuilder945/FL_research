import sys
num=eval(input())
num.sort()
ans=[]
if len(num)==1:
    print(num[0])
    sys.exit(0)
if num[0]!=num[1]:
    ans.append(num[0])
for i in range(1,len(num)-1):
    if num[i]!=num[i-1] and num[i]!=num[i+1]:
        ans.append(num[i])
if num[-1]!=num[-2]:
    ans.append(num[-1])
if len(ans)>=1:
    for i in range(len(ans)-1):
        print(ans[i],end=",")
    print(ans[-1])
else:
    print("False")


import sys
num=[int(i) for i in input().split(",")]
n,m=(int(i) for i in input().split(","))
if n>=len(num):
    print("error")
    sys.exit(0)
ans=num[n]
for i in range(m):
    num.append(ans)
print(num)


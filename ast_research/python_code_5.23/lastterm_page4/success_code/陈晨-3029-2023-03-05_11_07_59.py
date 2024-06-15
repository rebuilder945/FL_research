name=list(input().split(","))
num=eval(input())
n=len(num)
for x in range(n):
    name[x]=[name[x]]+[num[x]]
print(name)

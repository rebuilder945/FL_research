names=list(input().split(","))
num=eval(input())
n=len(num)
for x in range(n):
    names[x]=[names[x]+num[x]]
print(names)

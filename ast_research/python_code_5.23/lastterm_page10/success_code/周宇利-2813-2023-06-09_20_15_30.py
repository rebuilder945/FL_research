n=list(input().split())
m=input()
for i in n:
    if i==m:
        n.remove(m)
print((" ").join(n))

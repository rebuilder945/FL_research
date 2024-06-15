n=input().split(" ")
a,b=input().split(" ")
a=int(a)
b=int(b)
for x in n:
    n[a],n[b]=n[b],n[a]
print(list(n))

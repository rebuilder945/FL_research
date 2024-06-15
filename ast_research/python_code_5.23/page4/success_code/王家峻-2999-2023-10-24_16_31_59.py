n=eval(input().split())
a,b=eval(input())
n[b],n[a]=n[a],n[b]
print(n.split(","))

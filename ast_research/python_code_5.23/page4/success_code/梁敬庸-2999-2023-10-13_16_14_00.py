K=input()
K=list(K.split())
a,b=map(int,input().split())
c=K[a]
d=K[b]
K[a]=c
K[b]=d
print(K)

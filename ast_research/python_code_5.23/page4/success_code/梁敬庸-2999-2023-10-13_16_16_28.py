K=input()
K=list(K.split())
a,b=map(int,input().split())
L=K.copy()
K[a]=L[b]
K[b]=L[a]
print(K)

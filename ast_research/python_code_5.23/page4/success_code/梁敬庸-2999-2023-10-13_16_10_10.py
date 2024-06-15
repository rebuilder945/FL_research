K=input()
K=list(K.split())
a,b=eval(input())
c=K[a]
d=K[b]
K[a]=c
K[b]=d
print(K)

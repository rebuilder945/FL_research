n1=input().split()
n2,n3=map(int,input().split()) 
n1[n2],n1[n3]=n1[n3],n1[n2]
print(n1)

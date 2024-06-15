n=list(input())
n1=[]
for i in n:
    j=(int(i)+5)%10
    n1.append(j) 
for h in range(int(len(n1)/2)):
    n1[h],n1[-h-1]=n1[-h-1],n1[h]
n1=map(str,n1)
print("".join(n1))


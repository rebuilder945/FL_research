n=list(input())
n1=[]
for i in n:
    j=(int(i)+5)%10
    n1.append(j)
n1.reverse
n1=map(str,n1)
print("".join(n1))


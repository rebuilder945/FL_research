n1=input().split()
n4=input().split()
n2=int(n4[0])
n3=int(n4[1])
n1.insert(n2,n1[n3])
n1.insert(n3,n1[n2])
n1.pop(n2+1)
n1.pop(n3+1)
print(n1)



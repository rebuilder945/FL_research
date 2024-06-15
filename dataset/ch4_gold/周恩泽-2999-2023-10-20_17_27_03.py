# n1=input().split()
# n4=input().split()
# n2=int(n4[0])
# n3=int(n4[1])
# n11=n1.copy()
# del n11[n2]
# n11.insert(n3,n1[n2])
# del n11[n3-1]
# n11.insert(n2-1,n1[n3])
# print(n11)



n1=input().split()
n2,n3=map(int,input().split())
n1[n2],n1[n3]=n1[n3],n1[n2]
print(n1)

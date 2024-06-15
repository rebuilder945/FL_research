str1 = input()
li1 = list(map(int, str1.split(',')))
n,m=map(int,input().split(','))
for j in range(m):
    li1+=[li1[n]]
print(li1)


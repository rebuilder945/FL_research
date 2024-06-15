lis1 =list(input().split())
a,b =input().split()
a=int(a)
b=int(b)
lis1[a],lis1[b] = lis1[b],lis1[a]
print(lis1)

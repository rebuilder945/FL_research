line=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
line[n],line[m]=line[m],line[n]
print(line)

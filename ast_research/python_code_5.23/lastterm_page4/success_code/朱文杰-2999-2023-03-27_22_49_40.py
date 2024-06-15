s=input().split()
n,m=map(int,input().split())
temp=s[n]
s[n]=s[m]
s[m]=temp
print(s)

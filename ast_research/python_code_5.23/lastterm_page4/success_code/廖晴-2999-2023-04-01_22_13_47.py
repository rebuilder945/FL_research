s=input().split()
n,m=map(int,input().split())
a=s[n]
b=s[m]
s[n]=s[m]
s[m]=a
print(s)

n,m,l=eval(input())
a=[n]
s=n
while m>len(a):
    s+=l
    a.append(s)
print(a)


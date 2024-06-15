l=list(eval(input()))
n,m=eval(input())
a=l[n]
for i in range(m):
    if i<m:
        i=i+1
        l.append(a)
print(l)
if n>len(l) or m>len(l):
    print("error")
    
    

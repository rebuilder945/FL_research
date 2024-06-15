lst1=eval(input())
lst1.sort(reverse=True)
lst2=[]
m=str(0)
for t in lst1:
    n=str(t)
    m+=n
s=m[1:]
print(int(s))


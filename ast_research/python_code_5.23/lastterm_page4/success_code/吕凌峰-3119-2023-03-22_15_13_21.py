a=eval(input())
b=[]
length=len(a)
for i in range(length-1):
    n=0
    for x in b:
        if a[length-i-1]==x:
            n=1
    if n==0:
        b.append(a[length-i-1])
b.reverse()
print(b)




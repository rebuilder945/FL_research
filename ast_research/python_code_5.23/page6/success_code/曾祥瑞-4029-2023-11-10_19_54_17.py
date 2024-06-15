n,m=input().split()
n=int(n)
m=int(m)
a=[]
if n>m or n+3>m or m<0 or n<0:
    print("illegal input")
else:
    for i in range(n,m):
        for x in range(n,m):
            for y in range(n,m):
                if x!=y and x!=i and y!=i and y!=0:
                    c=100*i+10*x+y
                    a.append(c)
    for m in range(len(a)):
        print(a[m],end=' ')

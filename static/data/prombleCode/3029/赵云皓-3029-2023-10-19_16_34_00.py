a=input().split(",")
b=eval(input())
c=[]
for x in a:
    n=a.index(x)
    c.append([x,b[n]])
print(c)

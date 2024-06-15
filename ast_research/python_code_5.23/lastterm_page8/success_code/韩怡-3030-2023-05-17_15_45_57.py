a=input().split(",")
b=list(eval(input()))
c=[]
for x in range(0,len(a)):
    c.append([a[x],b[x]])
d=sorted(c)
print(c)


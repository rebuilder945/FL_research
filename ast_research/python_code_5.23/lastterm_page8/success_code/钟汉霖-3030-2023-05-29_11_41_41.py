a=input().split(",")
b=list(eval(input()))
b.sort(reverse=False)
c=[]
for x in range(0,len(a)):
    c.append([b[x],a[x]])
print(c)

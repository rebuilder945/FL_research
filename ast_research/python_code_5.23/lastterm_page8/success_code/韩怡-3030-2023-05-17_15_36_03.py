a=input().split(",")
b=list(eval(input()))
b.sort(reverse=False)
c=[]
for x in range(0,len(a)):
    c.append([a[x],b[x]])
print(c)


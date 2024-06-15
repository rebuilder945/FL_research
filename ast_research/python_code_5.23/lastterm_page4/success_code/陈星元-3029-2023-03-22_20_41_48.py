a=input().split(",")
b=eval(input())
c=[]
for x in range(len(b)+1):
    c.append([a[x],b[x]])
print(c)

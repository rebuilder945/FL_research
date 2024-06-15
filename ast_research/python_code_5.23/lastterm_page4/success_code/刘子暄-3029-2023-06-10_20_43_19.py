a=list(input().split(","))
b=eval(input())
c=[]
i=0
for x in a:
    c.append([x,b[i]])
    i +=1
print(c)


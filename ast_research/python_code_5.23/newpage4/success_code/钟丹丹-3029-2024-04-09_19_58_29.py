n=input().split(",")
m=eval(input())
a=[]
for x in n:
    for y in m:
        if n.index(x)==m.index(y):
            a.append([x,y])
print(a)           

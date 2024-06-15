x1=input().split(" ")
x3,x4=input().split(" ")
x5=int(x3)
x6=int(x4)
x2=list(x1)
y1=x2[x5]
y2=x2[x6]
x2[x5]=y2
x2[x6]=y1
print(x2)

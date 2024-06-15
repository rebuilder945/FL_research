x1=input().split(",")
x2=eval(input())
x3=list(x1)
x4=[[x3[i],x2[i]] for i in range(len(x2))]
print(x4)

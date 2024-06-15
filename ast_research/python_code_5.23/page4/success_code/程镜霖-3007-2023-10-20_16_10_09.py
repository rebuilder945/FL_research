x1=eval(input())
n,m=eval(input())
x3=[]
if n>m or n>len(x1):
    print("error")
else:
    for i in range(n,m):
        x3.append(x1[i])
x4=x1

for i in x3:
    x4.remove(i)
print(x4)

        

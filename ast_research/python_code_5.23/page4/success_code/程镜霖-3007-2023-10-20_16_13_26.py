x1=eval(input())
n,m=eval(input())
x3=[]
if n>m or n>len(x1)-1:
    print("error")
else:
    for i in range(n,m):
        x3.append(x1[i])
        for i in x3:
         x1.remove(i)
        print(x1)

        

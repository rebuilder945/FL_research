a=int(input())
b=int(input())
c=-a
for i in range(b):
    c=c+a*2
    a=a/2
    # print(a)
print("%.2f"%(c))


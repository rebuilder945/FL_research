a=eval(input())
b=[]
for i in range(1,a+1):
    b.append(i)
b.remove("1")
b.append("1")
print(b)

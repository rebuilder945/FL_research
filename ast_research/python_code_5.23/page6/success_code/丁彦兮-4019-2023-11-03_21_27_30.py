#a=input().split(",")
m=input()
a=[]
for x in m:
    a.append(x)
b=len(a)
n=[]
a.reverse()
for i in range(0,b):
   c=eval(a[i])
   c=(c+5)%10
   c=str(c)
   n.append(c)
print(n)

print("".join(str(i) for i in n))






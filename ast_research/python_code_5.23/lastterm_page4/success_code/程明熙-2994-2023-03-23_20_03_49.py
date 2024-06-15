l=input()
n,m=eval(input())
a=[]
c=[]
l1=l.split(",")
if n<=len(l1):
    a.append(l1[n])
    b=l1+a*m
    for i in range(0,len(b)):
        c.append(eval(b[i]))
    print(c)

else:
    print("error")

# print(l1)

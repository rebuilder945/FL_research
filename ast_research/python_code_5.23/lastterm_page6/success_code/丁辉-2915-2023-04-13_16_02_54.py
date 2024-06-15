a=eval(input())
b=[]
for x in range(100,a+1):
    c=str(x)
    if int(c[0])**3+int(c[1])**3+int(c[2])**3==x:
        b.append(c)
if len(b)==0:
    print("none")
if len(b)!=0:
    print(len(b))

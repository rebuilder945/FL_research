a=eval(input())
x=[]
if a in range(100,1000):
    for i in range(100,a+1):
        b,c,d=str(i)
        if int(b)**3+int(c)**3+int(d)**3==i:
            print(i)
            x.append(i)
elif a>=1000:
    for i in range(100,1000):
        b,c,d=str(i)
        if int(b)**3+int(c)**3+int(d)**3==i:
            print(i)
            x.append(i)

if x==[]:
    print("none")


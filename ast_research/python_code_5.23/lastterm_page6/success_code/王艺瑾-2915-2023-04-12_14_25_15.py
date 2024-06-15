a=eval(input())
x=[]
for i in range(100,a+1):
    b,c,d=str(i)
    if int(b)**3+int(c)**3+int(d)**3==i:
        print(i)
        i.append(x)
if x==[]:
    print("none")


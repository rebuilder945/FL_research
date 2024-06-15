x=int(input())
y=[]
for i in range(100,x+1):
    t=str(i)
    a=int(t[0]);b=int(t[1]);c=int(t[2])
    if a**3+b**3+c**3==i:
        print(i)
        y.append(i)
if y!=[]:
    pass
else:
    print("none")

a=eval(input())
x=[]
for i in range(100,a+1):
    b,c,d=str(i)
    if b**3+c**3+d**3==i:
        print(i)
        i.append(x)
if x==[]:
    print("none")


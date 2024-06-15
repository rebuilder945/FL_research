a=eval(input())
b=[]
if a<=100:
    print("none")
else:
    if a>=1000:
        a=999
    for i in range(100,a+1):
        if (i//100)**3+((i//10)%10)**3+(i%10)**3==i:
            b.append(i)
    print(b.split())












        



    









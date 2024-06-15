a=eval(input())
b=[]
if a<=100 or a>1000:
    print("none")
else:
    for i in range(100,a+1):
        if ((i//100)**3)*100+((i//10)%10)**3+(i%10)**3==i:
            b.append(i)
    print(b)












        



    









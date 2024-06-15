n=eval(input())
list=[]
if 0<n<=100:
    for i in range(100,n+1):
        if (i%10)^3+(i//10)^3==n:
          list.append(n)
        elif (i%10)^3+(i//10)^3!=n:
         pass
elif 100<n<=1000:
        for i in range(100,n+1):
            if (i%10)^3+(i%10//10)^3+(i//100)^3==n:
                list.append(n)
            elif (i%10)^3+(i%10//10)^3+(i//100)^3!=n:
                pass
else:
    pass
if len(list)==0:
        print("none")
else:
    for y in range(len(list)):
        print(list[y])

a=eval(input())
sum=0
for i in range(0,len(a)):
    sum+=a[i]
    b=sum/len(a)
    if type(b)==int:
        print("b")
    else:
        print("%2f."%b)

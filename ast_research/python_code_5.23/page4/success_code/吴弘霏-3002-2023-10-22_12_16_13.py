list=eval(input())
a=sum(list)%len(list)
if a==0:
    print("%d"%sum(list)/len(list))
else:
    print("%.2f"%sum(list)/len(list))


n1=eval(input())
n2=[]
for x in n1:
    if x>10:
       if  x %2  !=0 and x % 3!=0 and x %5!=0 and x%7!=0:
           n2.append(x)
    else:
        if x==3 or x==2 or x==5 or x==7:
           n2.append(x)
print(n2)


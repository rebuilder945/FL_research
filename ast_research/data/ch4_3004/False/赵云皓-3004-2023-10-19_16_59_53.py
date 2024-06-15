a=eval(input())
b=[]
for x in a:
    if x==2 or x==3 or x==5 or x==7:
        b.append(x)
    elif x%2==0 or x%3==0 or x%5==0 or x%7==0:
        b=b
    else:
        b.append(x)
print(b)

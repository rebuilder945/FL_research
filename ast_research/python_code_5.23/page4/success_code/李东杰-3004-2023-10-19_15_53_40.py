a=eval(input())
b=[]
for x in a:
    if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0 and x%13!=0 and x%17!=0 and x%19!=0:
        b.append(x)
    elif x==2  or x==3 or x==5 or x==7 or x==11 or x==13 or x==17 or x==19:
        b.append(x)
    else:
        continue
print(b)



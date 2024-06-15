a=eval(input())
b=[]
if a<0 or a%1!=0:
    print("illegal input")
else:
    for i in range(a+1):
        s=str(i)
        if i==2 or i==3 or i==5 or i==7:
            b.append(i)
        elif i==1:
            a=a
        elif i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and s[0]==s[-1]:
            b.append(i)
        else:
            a=a
b=list(map(str,b))
print(" ".join(b))


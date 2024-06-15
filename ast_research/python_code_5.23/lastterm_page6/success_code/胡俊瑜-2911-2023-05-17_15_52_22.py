a=input("")
b=[]
for x in a:
    y=0
    y=(int(x)+5)%10
    b.append(y)
b.reverse()
for x in b:
    print(x,end="")

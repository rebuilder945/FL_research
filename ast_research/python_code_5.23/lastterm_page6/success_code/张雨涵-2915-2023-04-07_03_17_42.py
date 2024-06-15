a=eval(input())
b=[]
if a>999:
    for i in range(100,999):
        c=list(str(i))
        if int(c[0])**3+int(c[1])**3+int(c[2])**3==i:
            b.append(i)
elif 100<a<=999:
    for i in range(100,a+1):
        c=list(str(i))
        if int(c[0])**3+int(c[1])**3+int(c[2])**3==i:
            b.append(i)
else:
    pass
if b!=[]:
    d="\n".join("%s"%j for j in b)
    print(d)
else:
    print("none")

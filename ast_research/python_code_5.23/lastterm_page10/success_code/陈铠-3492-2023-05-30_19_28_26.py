a=input()
if a =="":
    print("None")
else:
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    num=list(d.items())
    num.sort(key=lambda x:x[1])
    m,n=num[0]
    print(m)

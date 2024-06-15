
liebiao=input()
x=list(eval(liebiao))
k=input()
k=k.split(",")
k1=int(k[0])
k2=int(k[1])
if k1<=k2:
    del x[k1:k2]
    print(x)
else:
    print("error")

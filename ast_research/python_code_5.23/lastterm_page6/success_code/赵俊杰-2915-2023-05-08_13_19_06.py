n=eval(input())
fnlist=[]
for x in range(100,n+1):
    if int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3==x:
        fnlist.append(x)
    else:
        pass
if len(fnlist)==0:
    print("none")
else:
    for i in fnlist:
        print(i)


ls=input().split(" ")
n=int(ls[0])
m=int(ls[1])
nl=[]
if n>=m:
    print("illegal input")
elif m-n<=2:
    print("illegal input")
elif n>=0 and m>0: 
    for i in range(n,m):
        for x in range(n,m):
            if x!=i:
                for y in range(n,m):
                    if y!=i and y!=x:
                        new=str(i)+str(x)+str(y)
                        ls2=list(new)
                        if ls2[0]!='0':
                            nl.append(int(new))
    print((' ').join(str(i) for i in nl))
else:
    print("illegal input")







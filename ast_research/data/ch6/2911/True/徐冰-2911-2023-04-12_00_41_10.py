ls1=list(map(int,input()))
ls2=[]
for x in ls1:
    y=(x+5)%10
    ls2.append(y)
ls2.reverse()
ls3=[str(i) for i in ls2]
print("".join(ls3))

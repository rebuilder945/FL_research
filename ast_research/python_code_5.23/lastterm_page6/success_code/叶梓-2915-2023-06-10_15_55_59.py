
n=map(int,eval(input()))
ls=list(n)
ls2=[]
for n in range(100,1001):
    a=ls[0]**3+ls[1]**3+ls[2]**3
    if a==n:
        ls2.append(n)
if len(ls2)>0:
    for i in range(len(ls2)):
        print(ls2[i])
else:
    print("none")


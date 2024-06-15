n=int(input())
sums=[]
final=[]
for i in range(100,n+1):
    sums.append(int(i))
for x in sums:
    x=str(x)
    x1=int(x[0])
    x2=int(x[1])
    x3=int(x[2])
    if int(x)==(x1**3)+(x2**3)+(x3**3):
        final.append(int(x))
if len(final)!=0:
    for p in final:
        print(int(p))
else:
    print("none")


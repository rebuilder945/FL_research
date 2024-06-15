m=eval(input())
n=min(m,key=m.count)
j=0
for n in m:
    if int(n.count())==1:
        j+=1
if j==0:
    print("False")
else:
    print(n)


        








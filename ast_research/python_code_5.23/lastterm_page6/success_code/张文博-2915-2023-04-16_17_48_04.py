a=eval(input())
b=[]
for x in range(9):
    for j in range(9):
        for k in range(9):
            if x*x*x+j*j*j+k*k*k==x*100+j*10+k:
                b.append(x*x*x+j*j*j+k*k*k)
c=[x for x in range(a)]
for x in c:
    if x in b:
        print(x,end=" ") 


a,b=map(int,input().split())
if 0<=a<b<11 and b-a>=3:
    for i in range(a,b):
        for m in range(a,b):
            for n in range(a,b):
                if i!=m and m!=n and n!=i:
                    A=i*100+m*10+n
                    if A>99:
                        print(A,end=' ')
else:
    print("illegal input")

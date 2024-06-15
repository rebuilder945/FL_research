a,b=map(int,input().split())
a=int(a)
b=int(b)
if a>b or b-a<3 or a<0 or b<0:
    print("illegal input")
else:
    for x in range(a,b):
        for y in range(a,b):
            for z in range(a,b):
                if x!=y and y!=z and x!=z:
                    sum=100*x+10*y+z
                    if sum>99:
                        print(sum,end='')

a,b=map(int,input().split())
if 0<a<b and a-b>=3:
    for x in range(a,b):
        for y in range(a,b):
            for z in range(a,b):
                if x!=y and x!=z and x!=z:
                    c=x*100+y*10+z
                    if 99<c:
                        print(c,end=' ')
else:
    print("illegal input")

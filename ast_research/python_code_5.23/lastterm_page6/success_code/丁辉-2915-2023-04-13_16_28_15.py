a=eval(input())
if a<153:
    print("none")
else:
    for x in range(1,10):
        for y in range(0,10):
            for z in range(0,10):
                c=x*100+y*10+z
                d=x**3+y**3+z**3
                if c==d and a>=c:
                    print("%ld"%c)


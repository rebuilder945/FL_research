a=eval(input())
if a<=100:
    print('none')
elif a<1000:
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                b=i*100+j*10+k
                if b<=a and i**3+j**3+k**3==b:
                    print(a)



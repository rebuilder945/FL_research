a=eval(input())
f=False
for i in range(1,0):
    for j in range(10):
        for k in range(10):
            if i*100+j*10+k==i**3+j**3+k**3:
                print(100*i+10*j+k)
                f=True
if not f:
    print("none")

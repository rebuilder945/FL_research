a=eval(input())
if int(a) <=100:
    print("none")
else:
    for i in range(100,int(a)+1):
        s=len(str(i))
        for j in str(i):
            if int(j)**s==i:
                print("i")
            else:
                print("none")

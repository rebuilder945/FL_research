n,m = input().split()
if 0<=int(m)<10 and 0<=int(n)<10 and int(m)-int(n)>=3:
    sums=[]
    for x in list(range(int(n,int(m)))):
        for y in list(range(int(n),int(m))):
            for z in list(range(int(n),int(m))):
                if x != y and y != z and x != z and x != 0:
                    sums.append(str(x)+str(y)+str(z))
    print(" ".join(str(i) for i in sums))
else:
    print("illegal input")





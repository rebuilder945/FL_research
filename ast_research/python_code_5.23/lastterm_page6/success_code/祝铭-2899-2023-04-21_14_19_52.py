n = input()
nlist = []
if n[0] != '-' :
    m = int(n[0])
    p = int(n[2])
    if p - m < 3:
        print("illegal input")
    else:
        for i in range(p-m):
            nlist.append(m+i)
        for x in nlist:
            if x != 0:
                for y in nlist :
                    if y != x:
                        for z in nlist :
                            if z != x and z != y :
                                print(100*x+10*y+z,end=" ")
else:
    print("illegal input")

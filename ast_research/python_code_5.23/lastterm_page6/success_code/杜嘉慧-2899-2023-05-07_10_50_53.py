n = int()
m = int()
sums = []
if 0<=int(m)<10 and 0<=int(n)<10 and int(m)-int(n)>=3:
    for x in list(range(int(n,int(m)))):
        for y in list(range(int(n),int(m))):
            for z in list(range(int(n),int(m))):
                if x != y and y != z and x != z and x != 0:
                    s1 = str(sums[x]) + str(sums[y]) + str(sums[z])
                    sums.append(s1)
                    print("".join(str(i)for i in sums))
else:
    print("illegal input")





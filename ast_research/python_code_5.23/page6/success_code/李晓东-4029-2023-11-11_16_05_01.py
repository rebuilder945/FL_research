n ,m = input().split("")
list = []
if n<m and m-n>=3:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    a = 100*x+10*y+z
                    list.append(a)
    for b in list:
        print("%d"%y,end = "")
else:
    print("illegai input")






n,m = input().split()
n = int(n)
m = int(m)
if m-n >= 3 and n>=0 and m<10 :
    for i in range(1,m):
        for x in range(n,m):
            for y in range(n,m):
                if i!=x and x!=y and i!=y :
                    print(f"{i}{x}{y}",end=" ")
else:
    print("illegal input")

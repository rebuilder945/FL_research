n,m = input().split()
n = int(n)
m = int(m)
if m-n >= 3:
    for i in range(n,m):
        for x in range(n,m):
            for y in range(n,m):
                if i!=x and x!=y and i!=y:
                    print(f"{i}{x}{y}")
else:
    print("illegal input")

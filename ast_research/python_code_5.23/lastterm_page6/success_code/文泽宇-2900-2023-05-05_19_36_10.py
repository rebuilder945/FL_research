n = eval(input())
if n>0 and type(n) == int:
    for m in range(2,n):
        count = 0
        for i in  range(2,m):
            if m%i == 0:
                count += 1
            continue
        if count == 0:
            sb = str(n)
            if sb == sb[::-1]:
                print(sb,end=" ")
else:
    print("illegal input")

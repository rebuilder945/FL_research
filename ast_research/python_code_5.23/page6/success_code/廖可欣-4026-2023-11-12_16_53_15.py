n = int(input())
kong = [2]
kong2 = [2]
for i in range(1,n+1):
        if i == 1:
                pass
        else:
            x = kong2[-1]+i-1
            end = x/i
            kong.append(end)
            kong2.append(x)
print("%.4f"%(sum(kong)))

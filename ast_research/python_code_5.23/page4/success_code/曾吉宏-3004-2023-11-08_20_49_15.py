ls = eval(input())
x = []
for i in ls:
    if i >= 2:
        for j in range(2,i):
            if i/j==0:
                break
        else:
            x.append(i)
print(x)


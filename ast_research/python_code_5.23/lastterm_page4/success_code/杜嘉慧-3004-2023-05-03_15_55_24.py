lst = eval(input())
new=[]
for x in lst:
    if x >= 2:
        for j in range(2, x ):
            if x % j == 0 :
                break
        else:
            new.append(x)
print(new)


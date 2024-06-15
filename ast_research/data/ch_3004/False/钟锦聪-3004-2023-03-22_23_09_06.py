sums = eval(input())
sum = []
for x in sums:
    if x>3:
        for i in range(2,x//2+1):
            if x % i !=0:
                sum.append(x)
    if x ==2 or x==3:
        sum.append(x)
print(sum)


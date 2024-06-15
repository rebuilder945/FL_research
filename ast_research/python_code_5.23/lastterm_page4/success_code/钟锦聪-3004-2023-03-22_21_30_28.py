sums = eval(input())
sum = sums.copy()
for x in sums:
    if x <2:
        sum.remove(x)
for x in sums:
    if x>= 2 :
        for i in range(2,x//2+1):
            if x % i ==0:
                sum.remove(x)
print(sum)

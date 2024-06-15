sum = eval(input())
for x in sum:
    if x>= 2 :
        for i in range(2,x//2+1):
            if x % i ==0:
                sum.remove(x)
print(sum)

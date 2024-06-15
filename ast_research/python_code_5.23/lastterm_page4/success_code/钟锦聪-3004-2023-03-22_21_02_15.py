from os import remove


sums = eval(input())
sum = sums.copy()
if "1" in sums:
    sum.remove("1")
for x in sums:
    if x>= 2 :
        for i in range(2,x//2+1):
            if x % i ==0:
                sum.remove(x)
print(sum)

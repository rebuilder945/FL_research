n = int(input())
sum = 0
for ciShu in range(1,4):
    if ciShu==1:
        sum +=n
    else:
        n /=2
        sum += n*2
print(sum)
print(n)

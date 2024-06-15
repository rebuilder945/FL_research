sums = list(eval(input()))
n, m = eval(input())
if n >= (-len(sums)) and n < len(sums):
    x = sums[n]
    sums = sums + [x] * m
    print(sums)
else:
    print("error")

sum = []
a = eval(input())
b = min(a)
c = max(a)
for x in a:
    if x!=b and x!=c:
        sum.append(x)
print(sum)

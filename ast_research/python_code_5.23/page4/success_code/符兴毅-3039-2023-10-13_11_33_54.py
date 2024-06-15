lis = eval(input())
num_max = lis.count(max(lis))
num_min = lis.count(min(lis))
for i in range(num_max):
    lis.remove(max(lis))
try:
    for b in range(num_min):
        lis.remove(min(lis))
except ValueError:
    print(lis)
    a = 1
if a == 1:
    pass
else:
    print(lis)


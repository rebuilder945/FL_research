lis = eval(input())
num_max = lis.count(max(lis))
num_min = lis.count(min(lis))
for i in range(num_max):
    lis.remove(max(lis))
if lis == True:
    for b in range(num_min):
        lis.remove(min(lis))
else:
    print(lis)


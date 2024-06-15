lis = eval(input())
# lis.remove(max(lis))  #.remove只删除一个
# lis.remove(min(lis))
num_max = lis.count(max(lis))
num_min = lis.count(max(lis))
for i in range(num_max):
    lis.remove(max(lis))
for b in range(num_min):
    lis.remove(min(lis))
print(lis)

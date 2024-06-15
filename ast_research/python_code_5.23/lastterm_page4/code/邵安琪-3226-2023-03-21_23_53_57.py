def search(x):
for i in range(len(x)):
    a = count(x[i])
if a>len(x)//2:
    return a
else:
    return"False"






nums = eval(input())
y = search(nums)
print(y)



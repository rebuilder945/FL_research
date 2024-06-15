nums = eval(input())
kong = []
ling = []
for i in nums:
    if i == 0:
        ling.append(i)
    else:
        kong.append(i)
end = kong+ling
print(end)

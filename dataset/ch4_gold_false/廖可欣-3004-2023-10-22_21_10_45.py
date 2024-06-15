nums = eval(input())
kong = []
end = []
for i in nums:
    for r in range(2,i):
        while i%r != 0:
            break
        else:
            kong.append(i)
for i in nums:
    if i in kong:
        pass
    else:
        end.append(i)
print(end)

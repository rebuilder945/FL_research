m = str(input())
nums = []
end = "q"
for x in range(len(m)):
    nums.append(x)
lis = []
for i in nums:
    a = nums.count(i)
    lis.append(a)
for x in nums:
    if nums.count(x)==max(lis):
        print(x,max(lis))
        break

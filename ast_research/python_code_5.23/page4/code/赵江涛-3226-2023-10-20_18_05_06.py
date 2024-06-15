def search():
 for num, freq in count.items():
    if freq > len(nums) // 2:
        return num

return False






nums = eval(input())
y = search(nums)
print(y)



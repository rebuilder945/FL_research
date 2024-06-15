from audioop import reverse
nums=eval(input())
nums.sort(reverse=True)
num_str="".ioin(str(x) for x in nums)
print(int(num_str))


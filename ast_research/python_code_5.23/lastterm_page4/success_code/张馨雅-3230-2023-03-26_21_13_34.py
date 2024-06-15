nums=eval(input())
nums.sort(reverse=True)
a=[str(i) for i in nums]
b=int(''.join(a))
# for i in nums:
#     out.append(i)
print(b)

nums_str=input()
new_nums=[]
for i in range(len(nums_str)):
    new_nums.append((int(nums_str[i])+5)%10)
new_nums.reverse()
print("".join(str(x) for x in new_nums))

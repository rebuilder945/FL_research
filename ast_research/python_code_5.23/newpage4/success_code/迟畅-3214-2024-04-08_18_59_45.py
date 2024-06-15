nums =eval(input())
zero_count =nums.count(0)

while nums.count(0)>0:
    nums .remove(0)
zero_l=[0]*zero_count
nums =nums+zero_l
print(nums)



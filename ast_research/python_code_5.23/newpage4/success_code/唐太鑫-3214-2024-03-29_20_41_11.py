nums=eval(input())
zero=nums.count(0)
while zero > 0:
    nums.remove(0)
zeros=[0]*zero
lst=nums+zeros
print(lst)


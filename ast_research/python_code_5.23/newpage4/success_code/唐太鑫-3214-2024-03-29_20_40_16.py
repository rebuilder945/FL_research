nums=eval(input())
zero=nums.count(0)
while nums.count(0) > 0:
    nums.remove(0)
zeros=[0]*a
lst=nums+zeros
print(lst)


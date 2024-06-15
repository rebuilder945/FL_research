bst=[]
def calDegrees(lst):
     for x in lst:
         bst.append(lst.count(x))
     return max(bst)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


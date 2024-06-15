# a=eval(input())
# c=[]
# d=[]
# for i in a:
#     b=a.count(i)
#     if b==1:
#         c.append(i)
#     if b!=1:
#         d.append(i)
#         if a==d:
#             print('False')
# print(c)
def find_unique_elements(nums):
    unique_elements = []
    for num in nums:
        if nums.count(num) == 1:
            unique_elements.append(num)
    
    if not unique_elements:
        return False
    
    return sorted(unique_elements)


